#!/usr/bin/env bash
# build.sh

set -o errexit

pip install -r requirements.txt

# Initialize database
python init_db.py
python seed_data.py

echo "✅ Build completed successfully!"