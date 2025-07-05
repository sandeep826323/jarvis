@echo off
echo Building Jarvis executable...
echo.

REM Ensure PyInstaller is installed
pip install pyinstaller

REM Clean previous builds
if exist "dist\Jarvis.exe" (
    echo Removing previous build...
    del /q "dist\Jarvis.exe"
)
if exist "dist\main.exe" (
    echo Removing previous build...
    del /q "dist\main.exe"
)

REM Build with PyInstaller
echo Building executable with PyInstaller...
pyinstaller --clean jarvis.spec

echo.
if exist "dist\Jarvis.exe" (
    echo Build successful! Your Jarvis.exe file is in the dist folder.
    echo.
    echo To run Jarvis.exe, simply double-click on it or run it from the command line.
    echo The executable will automatically check for and install any missing dependencies.
) else if exist "dist\main.exe" (
    echo Build successful! Your main.exe file is in the dist folder.
    echo.
    echo To run main.exe, simply double-click on it or run it from the command line.
    echo The executable will automatically check for and install any missing dependencies.
    
    REM Rename to Jarvis.exe if desired
    echo Renaming main.exe to Jarvis.exe...
    ren "dist\main.exe" "Jarvis.exe"
    if exist "dist\Jarvis.exe" (
        echo Successfully renamed to Jarvis.exe
    ) else (
        echo Failed to rename executable
    )
) else (
    echo Build failed. Please check the error messages above.
)

pause 