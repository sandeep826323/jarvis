@echo off
echo Starting Jarvis...

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies if requirements.txt exists
if exist "Requirements.txt" (
    echo Checking/installing dependencies...
    pip install -r Requirements.txt
)

REM Run the main application
echo Starting the application...
python Main.py

REM Keep the window open if there's an error
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo An error occurred. Press any key to exit.
    pause >nul
) 