# analysis-service/tests/test_analysis_routes.py
import unittest
from unittest.mock import patch
import json
from app import app

class TestAnalysisRoutes(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    @patch('routes.analysis_routes.calculate_moving_averages')
    def test_get_analysis_success(self, mock_calculate):
        """Test successful analysis retrieval"""
        mock_calculate.return_value = {
            'ticker': 'AAPL',
            'current_price': 150.25,
            'ma_7': 149.0,
            'ma_30': 148.0,
            'signal': 'BUY'
        }
        
        response = self.app.get('/api/analysis/AAPL')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['ticker'], 'AAPL')
        self.assertEqual(data['signal'], 'BUY')
    
    @patch('routes.analysis_routes.calculate_moving_averages')
    def test_get_analysis_error(self, mock_calculate):
        """Test analysis with error"""
        mock_calculate.side_effect = Exception("Analysis failed")
        
        response = self.app.get('/api/analysis/INVALID')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 500)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()