# backend/tests/test_stock_routes.py
import unittest
from unittest.mock import patch, MagicMock
import json
from app import app

class TestStockRoutes(unittest.TestCase):
    
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True
    
    @patch('routes.stock_routes.get_stock_info')
    @patch('routes.stock_routes.requests.get')
    def test_stock_info_success(self, mock_requests, mock_get_stock):
        """Test successful stock info retrieval"""
        # Mock stock service
        mock_get_stock.return_value = (150.25, [
            {'Date': '2024-01-01', 'Close': 150.0}
        ])
        
        # Mock analysis service
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'ticker': 'AAPL',
            'ma_7': 149.0,
            'ma_30': 148.0,
            'signal': 'BUY'
        }
        mock_requests.return_value = mock_response
        
        # Make request
        response = self.app.get('/api/stock/AAPL')
        data = json.loads(response.data)
        
        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['ticker_symbol'], 'AAPL')
        self.assertEqual(data['current_price'], 150.25)
        self.assertIn('analysis', data)
    
    @patch('routes.stock_routes.get_stock_info')
    def test_stock_info_invalid_ticker(self, mock_get_stock):
        """Test with invalid ticker"""
        mock_get_stock.side_effect = Exception("Invalid ticker")
        
        response = self.app.get('/api/stock/INVALID')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 500)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()