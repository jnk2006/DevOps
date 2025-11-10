from flask import Blueprint, jsonify
import requests
from service.stock_service import get_stock_info

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/stock/<ticker_symbol>', methods=['GET'])
def stock_info(ticker_symbol):
    try:
        # Get stock data from your service
        current_price, past_30_days = get_stock_info(ticker_symbol)
        
        # Call the analysis microservice
        analysis_data = None
        try:
            print(f"Calling analysis service for {ticker_symbol}...")
            analysis_response = requests.get(
                f'http://localhost:5001/api/analysis/{ticker_symbol}',
                timeout=5
            )
            print(f"Analysis response status: {analysis_response.status_code}")
            
            if analysis_response.status_code == 200:
                analysis_data = analysis_response.json()
                print(f"Analysis data: {analysis_data}")
            else:
                print(f"Analysis service returned error: {analysis_response.text}")
        except Exception as e:
            print(f"Error calling analysis service: {str(e)}")
            analysis_data = None
        
        response = {
            'ticker_symbol': ticker_symbol.upper(),
            'current_price': current_price,
            'past_30_days': past_30_days,
            'analysis': analysis_data
        }
        
        print(f"Final response: {response}")
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500