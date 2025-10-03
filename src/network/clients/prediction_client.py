import requests 
TOKEN = ""

class PredictionClient: 
    def __init__(self, url="http://localhost:8080/", token=TOKEN, timeouts=10):
        self.url = url 
        self.token = token 
        self.timeouts = timeouts

    def send_predictions(self, predictions_dict: dict) -> None: 
        """
        Sends ML predictions to the backend for storage/execution.
        
        Args:
            predictions_dict: {
                'symbol': str,
                'prediction_value': float,  # The ML model prediction
                'confidence': float,  # Model confidence score (0-1)
                'timestamp': datetime  # When prediction was generated
            }
        
        Returns:
            dict: {
                'success': bool,
                'data': dict | None,  # Backend response if successful
                'error': str | None,
                'timestamp': datetime
            }
        """
        pass
        
