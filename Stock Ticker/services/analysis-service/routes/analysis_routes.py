# This imports from stock_routes.py and defines the routes:

from flask import Blueprint, jsonify
from service.analysis_service import calculate_moving_averages

analysis_bp = Blueprint('analysis', __name__)
@analysis_bp.route('/analysis/<ticker_symbol>', methods=['GET'])

def stock_analysis(ticker_symbol):
    try:
        analysis_result = calculate_moving_averages(ticker_symbol)
        return jsonify(analysis_result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500