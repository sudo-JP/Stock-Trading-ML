use std::ffi::CString;
use nix::unistd::{fork, ForkResult, pipe, close};
use nix::sys::wait::waitpid;
use nix::unistd::execvp;

use nix::unistd::{write, read}; 
use std::os::fd::AsRawFd;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let (read_fd, write_fd) = pipe()?;
    unsafe {
        match fork() {
            Ok(ForkResult::Parent{child}) => {
                nix::unistd::close(read_fd)?;
                let data = b"Pipe content";
                write(write_fd.as_raw_fd(), data)?;
                waitpid(child, None)?;
            }, 
            Ok(ForkResult::Child) => {
                close(write_fd)?;

                let program = CString::new("python3")?;
                let script = CString::new("app/main.py")?;
                let mut args = vec![program.clone(), script]; 

                let mut buffer = vec![0; 13]; 
                let bytes_read = read(read_fd.as_raw_fd(), &mut buffer)?; 
                buffer.truncate(bytes_read); 
                let buffer_str = String::from_utf8(buffer)?;
                let buffer_cstr = CString::new(buffer_str)?;
                args.push(buffer_cstr);
                execvp(&program, &args)?;
            },
            Err(e) => eprint!("{}", e)
        }

    }
    Ok(())
}
