#!/bin/bash
# Sets up a Python virtual environment and installs dependencies.
# Run this script from the project root folder.
# On Windows, run it using Git Bash.

python3 -m venv venv

# Activate the virtual environment
if [ -f "venv/Scripts/activate" ]; then
    # Windows (Git Bash)
    source venv/Scripts/activate
else
    # Mac / Linux
    source venv/bin/activate
fi

pip install -r requirements.txt

echo ""
echo "Setup complete. Virtual environment is ready."
echo "To activate it later, run:"
echo "  source venv/bin/activate   (Mac/Linux)"
echo "  source venv/Scripts/activate   (Windows Git Bash)"
