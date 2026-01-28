# analysis-service/tests/test_analysis_service.py
import unittest
from unittest.mock import patch, MagicMock
from service.analysis_service import calculate_moving_averages, get_signal
import pandas as pd
import numpy as np

class TestAnalysisService(unittest.TestCase):
    
    @patch('service.analysis_service.yf.Ticker')
    def test_calculate_moving_averages_valid(self, mock_ticker):
        """Test MA calculation with valid data"""
        # Create mock data with 60 days
        dates = pd.date_range('2024-01-01', periods=60)
        prices = np.linspace(140, 160, 60)  # Upward trend
        
        mock_stock = MagicMock()
        mock_history = pd.DataFrame({
            'Close': prices
        }, index=dates)
        
        mock_stock.history.return_value = mock_history
        mock_ticker.return_value = mock_stock
        
        result = calculate_moving_averages('AAPL')
        
        self.assertEqual(result['ticker'], 'AAPL')
        self.assertIsNotNone(result['ma_7'])
        self.assertIsNotNone(result['ma_30'])
        self.assertIn(result['signal'], ['BUY', 'SELL', 'HOLD'])
    
    @patch('service.analysis_service.yf.Ticker')
    def test_calculate_moving_averages_insufficient_data(self, mock_ticker):
        """Test with insufficient data for MA30"""
        dates = pd.date_range('2024-01-01', periods=10)
        prices = [150.0] * 10
        
        mock_stock = MagicMock()
        mock_history = pd.DataFrame({
            'Close': prices
        }, index=dates)
        
        mock_stock.history.return_value = mock_history
        mock_ticker.return_value = mock_stock
        
        result = calculate_moving_averages('AAPL')
        
        # MA30 should be None with only 10 days of data
        self.assertIsNone(result['ma_30'])
        self.assertEqual(result['signal'], 'INSUFFICIENT_DATA')
    
    def test_get_signal_buy(self):
        """Test BUY signal generation"""
        signal = get_signal(price=155, ma7=152, ma30=150)
        self.assertEqual(signal, 'BUY')
    
    def test_get_signal_sell(self):
        """Test SELL signal generation"""
        signal = get_signal(price=145, ma7=148, ma30=150)
        self.assertEqual(signal, 'SELL')
    
    def test_get_signal_hold(self):
        """Test HOLD signal generation"""
        signal = get_signal(price=150, ma7=152, ma30=148)
        self.assertEqual(signal, 'HOLD')
    
    def test_get_signal_insufficient_data(self):
        """Test signal with NaN values"""
        signal = get_signal(price=150, ma7=np.nan, ma30=150)
        self.assertEqual(signal, 'INSUFFICIENT_DATA')

if __name__ == '__main__':
    unittest.main()