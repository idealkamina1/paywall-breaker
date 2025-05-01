#!/bin/bash

# This script sets up the development environment for the paywall breaker project.

# Update package list and install necessary packages
sudo apt-get update
sudo apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required Python packages
pip install -r ../requirements.txt

# Inform the user that the setup is complete
echo "Development environment setup complete. Activate the virtual environment using 'source venv/bin/activate'."