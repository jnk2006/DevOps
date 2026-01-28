#!/bin/bash

# Start backend
cd services/backend
python app.py &
BACKEND_PID=$!

# Start analysis service
cd ../analysis-service
python app.py &
ANALYSIS_PID=$!

echo "Backend running on PID: $BACKEND_PID"
echo "Analysis running on PID: $ANALYSIS_PID"
echo "Press Ctrl+C to stop all services"

# Wait for Ctrl+C
trap "kill $BACKEND_PID $ANALYSIS_PID; exit" INT
wait