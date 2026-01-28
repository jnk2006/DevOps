# backend/tests/test_stock_service.py
import unittest
from unittest.mock import patch, MagicMock
from service.stock_service import get_stock_info
import pandas as pd

class TestStockService(unittest.TestCase):
    
    @patch('service.stock_service.yf.Ticker')
    def test_get_stock_info_valid_ticker(self, mock_ticker):
        """Test getting stock info with valid ticker"""
        # Mock the yfinance response
        mock_stock = MagicMock()
        
        # Create mock data with dates as INDEX (like real yfinance)
        dates = pd.date_range('2024-01-01', periods=30)
        mock_history = pd.DataFrame({
            'Close': [150.0 + i for i in range(30)]  # Prices from 150 to 179
        }, index=dates)
        mock_history.index.name = 'Date'  # Important: set index name
        
        mock_stock.history.return_value = mock_history
        mock_ticker.return_value = mock_stock
        
        # Call the function
        current_price, past_30_days = get_stock_info('AAPL')
        
        # Assertions
        self.assertEqual(current_price, 150.0)  # First day's price
        self.assertEqual(len(past_30_days), 30)
        self.assertIn('Date', past_30_days[0])
        self.assertIn('Close', past_30_days[0])
        
        # Check date format
        self.assertRegex(past_30_days[0]['Date'], r'\d{4}-\d{2}-\d{2}')
        
        mock_ticker.assert_called_with('AAPL')
    
    @patch('service.stock_service.yf.Ticker')
    def test_get_stock_info_invalid_ticker(self, mock_ticker):
        """Test getting stock info with invalid ticker"""
        mock_stock = MagicMock()
        mock_stock.history.return_value = pd.DataFrame()  # Empty dataframe
        mock_ticker.return_value = mock_stock
        
        # Should raise an exception (KeyError or IndexError)
        with self.assertRaises((KeyError, IndexError, Exception)):
            get_stock_info('INVALID')
    
    @patch('service.stock_service.yf.Ticker')
    def test_get_stock_info_network_error(self, mock_ticker):
        """Test handling network errors"""
        mock_ticker.side_effect = Exception("Network error")
        
        with self.assertRaises(Exception):
            get_stock_info('AAPL')
    
    @patch('service.stock_service.yf.Ticker')
    def test_get_stock_info_single_day(self, mock_ticker):
        """Test with single day of data"""
        mock_stock = MagicMock()
        
        dates = pd.date_range('2024-01-01', periods=1)
        mock_history = pd.DataFrame({
            'Close': [150.25]
        }, index=dates)
        mock_history.index.name = 'Date'
        
        mock_stock.history.return_value = mock_history
        mock_ticker.return_value = mock_stock
        
        current_price, past_30_days = get_stock_info('AAPL')
        
        self.assertEqual(current_price, 150.25)
        self.assertEqual(len(past_30_days), 1)

if __name__ == '__main__':
    unittest.main()