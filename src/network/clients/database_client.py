from datetime import datetime
from typing import Any
import requests

TOKEN = ""

class DatabaseClient: 
    def __init__(self, url="http://localhost:8080/", token=TOKEN, timeouts=10): 
        self.url = url  
        self.token = token 
        self.timeouts = timeouts


    def get_historical_data(self, symbol: str, start_date: datetime, end_date: datetime) -> dict:
        """
        Fetches historical market data for a symbol between dates.

        Args:
            symbol: Trading symbol (e.g., 'AAPL')
            start_date: Start of date range (inclusive)
            end_date: End of date range (inclusive)

        Returns:
            dict: {
                'success': bool,  # True if request succeeded
                'data': list[dict] | None,  # List of market data records if success
                'error': str | None,  # Error message if success=False
                'timestamp': datetime  # When this response was generated
            }
            
        Example success:
            {
                'success': True,
                'data': [
                    {'time': '2024-01-01T10:00:00', 'symbol': 'AAPL', 'price': 150.0},
                    {'time': '2024-01-01T10:01:00', 'symbol': 'AAPL', 'price': 150.5}
                ],
                'error': None,
                'timestamp': '2024-01-02T14:30:00'
            }
            
        Example failure:
            {
                'success': False, 
                'data': None,
                'error': 'Network timeout connecting to backend',
                'timestamp': '2024-01-02T14:30:00'
            }
        """
        pass
        
    def get_latest_market_data(self, symbols: list[str]) -> dict: 
        """
        Fetches latest market data for multiple symbols.
        
        Args:
            symbols: List of trading symbols (e.g., ['AAPL', 'GOOGL'])
        
        Returns:
            dict: {
                'success': bool,
                'data': dict[str, dict] | None,  # symbol -> latest data mapping
                'error': str | None,
                'timestamp': datetime
            }
            
        Example success:
            {
                'success': True,
                'data': {
                    'AAPL': {'bid': 150.0, 'ask': 150.1, 'last': 150.05},
                    'GOOGL': {'bid': 2700.0, 'ask': 2700.5, 'last': 2700.2}
                },
                'error': None,
                'timestamp': '2024-01-02T14:30:00'
            }
        """
        pass
