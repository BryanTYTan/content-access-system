VENV_DIR=".venv"

FLASK_APP_FILE="app.py"

if [ -d "$VENV_DIR" ]; then
    # Standard activation path for Unix/macOS
    source "$VENV_DIR/bin/activate"
    echo "Virtual environment activated."
else
    echo "Error: Virtual environment directory '$VENV_DIR' not found."
    exit 1
fi

cd Flask_app/

python3 app.py