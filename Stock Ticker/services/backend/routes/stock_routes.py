# This imports from stock_service.py and defines the routes:

from flask import Blueprint, request, jsonify
from service.stock_service import get_stock_info

stock_bp = Blueprint('stock', __name__)
@stock_bp.route('/stock/<ticker_symbol>', methods=['GET'])

def stock_info(ticker_symbol):
    try:
        current_price, past_30_days = get_stock_info(ticker_symbol)
        response = {
            'ticker_symbol': ticker_symbol.upper(),
            'current_price': current_price,
            'past_30_days': past_30_days
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500