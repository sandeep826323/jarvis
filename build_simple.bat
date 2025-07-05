@echo off
echo Building Jarvis executable (simple version)...
echo.

REM Ensure PyInstaller is installed
pip install pyinstaller

REM Clean previous builds
if exist "dist\Jarvis.exe" (
    echo Removing previous build...
    del /q "dist\Jarvis.exe"
)

REM Build with PyInstaller
echo Building executable with PyInstaller...
pyinstaller --clean jarvis_simple.spec

echo.
if exist "dist\Jarvis.exe" (
    echo Build successful! Your Jarvis.exe file is in the dist folder.
    echo.
    echo To run Jarvis.exe, simply double-click on it or run it from the command line.
    echo The executable will automatically check for and install any missing dependencies.
) else (
    echo Build failed. Please check the error messages above.
)

pause 