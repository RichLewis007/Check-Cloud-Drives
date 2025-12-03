#!/usr/bin/env bash
# Run script for Check Cloud Drives application

set -e

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Error: uv is not installed."
    echo "Please install uv first:"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Sync dependencies if needed (creates venv if it doesn't exist)
if [ ! -d ".venv" ]; then
    echo "Setting up virtual environment and installing dependencies..."
    uv sync
fi

# Run the application
echo "Starting Check Cloud Drives..."
uv run -m check_cloud_drives.main


