'''
Calculates technical indicators (RSI, Moving Averages, etc.) for a stock - Micro service 2
This is where:

Initialize web framework (Flask, FastAPI, etc.)
Register routes
Configure middleware
Start the server


Flow:

app.py starts the server and registers routes
Request comes in -> stock_routes.py handles it
Route calls function from stock_service.py
Result flows back to the frontend

This separation keeps your code organized: app.py (setup) -> routes (endpoints) -> services (business logic)

RUN ON PORT 5001
'''

from flask import Flask, jsonify, render_template
from routes.analysis_routes import analysis_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(analysis_bp, url_prefix='/api')

# Serve the frontend
if __name__ == '__main__':
    app.run(debug=True, port=5001)
