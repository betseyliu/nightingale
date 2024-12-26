#!/bin/bash

# Set environment variables
export FLASK_APP="app.py"
export FLASK_DEBUG=1
export FLASK_ENV="development"
export FLASK_SQLALCHEMY_DATABASE_URI="sqlite:///database.db"
export FLASK_SECRET_KEY="florence-nightingale-memorial-key"

# Do cleanup
find . -type d -name "__pycache__" -prune -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true
find . -type f -name "*.db" -delete 2>/dev/null || true
find . -type f -name "*.sqlite" -delete 2>/dev/null || true

# Install dependencies
echo "Installing dependencies..."
cd /app
poetry config virtualenvs.create false
poetry install --no-interaction --no-ansi

# Initialize data
echo "Initializing data..."
flask cli init-db

# Start backend service(s)
echo "Starting backend service(s)..."
cd /app
flask run --host=0.0.0.0 --port=8888 &

# Note: No frontend service to start as there's no package.json or frontend framework configuration

echo "Application startup complete."

# Wait for any background services
tail -f /dev/null