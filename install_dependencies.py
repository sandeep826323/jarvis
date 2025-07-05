import sys
import subprocess
import importlib.util
import os

def check_module(module_name):
    """Check if a module is installed."""
    try:
        # Handle special cases for package names different from import names
        if module_name == "python-dotenv":
            module_name = "dotenv"
        elif module_name == "googlesearch-python":
            module_name = "googlesearch"
        elif module_name == "opencv-python":
            module_name = "cv2"
        elif module_name == "pillow":
            module_name = "PIL"
            
        return importlib.util.find_spec(module_name) is not None
    except (ImportError, AttributeError):
        return False

def install_module(module_name):
    """Install a module using pip."""
    print(f"Installing missing module: {module_name}")
    try:
        # Use sys.executable to ensure we use the correct Python interpreter
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        return True
    except subprocess.CalledProcessError:
        print(f"Failed to install {module_name}")
        return False

def check_and_install_requirements():
    """Check all requirements and install missing ones."""
    # Get the script's directory
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        base_path = os.path.dirname(sys.executable)
    else:
        # Running as script
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    requirements_path = os.path.join(base_path, "Requirements.txt")
    
    # Check if Requirements.txt exists
    if not os.path.exists(requirements_path):
        print("Requirements.txt not found. Creating default requirements file.")
        required_modules = [
            "python-dotenv>=1.0.0", "groq", "AppOpener", "pywhatkit", "bs4",
            "pillow", "rich", "requests", "keyboard", "cohere", 
            "googlesearch-python", "selenium", "mtranslate", "pygame",
            "edge-tts", "PyQt5", "webdriver-manager", "asyncio", 
            "instagrapi>=2.0.0", "pyttsx3", "opencv-python", "face_recognition",
            "numpy", "yfinance", "SpeechRecognition", "pyaudio", "twilio", 
            "pytube", "tensorflow", "pandas", "scikit-learn", "tensorflow-hub",
            "tensorflow-text", "matplotlib", "psutil", "scipy", "h5py"
        ]
        
        # Create a default Requirements.txt file
        with open(requirements_path, 'w') as file:
            for module in required_modules:
                file.write(f"{module}\n")
    
    # Read requirements
    with open(requirements_path, 'r') as f:
        requirements = [line.strip() for line in f.readlines() if line.strip()]
    
    missing_modules = []
    
    # Check each requirement
    for req in requirements:
        # Extract the module name from the requirement string
        module_name = req.split('>=')[0].split('==')[0].split('<')[0].strip()
        if not check_module(module_name):
            missing_modules.append(req)
    
    # Install missing modules
    if missing_modules:
        print(f"Found {len(missing_modules)} missing modules. Installing...")
        for module in missing_modules:
            install_module(module)
        print("All missing dependencies have been installed.")
    else:
        print("All dependencies are already installed.")

if __name__ == "__main__":
    check_and_install_requirements()
    
    # Start the main application
    print("Starting main application...")
    if getattr(sys, 'frozen', False):
        # If running as frozen executable, the main script is already part of it
        # No need to do anything here as PyInstaller will handle this
        pass
    else:
        # If running as script, launch Main.py
        try:
            import Main
        except ImportError as e:
            print(f"Error importing Main module: {e}")
            # Fallback to subprocess
            subprocess.call([sys.executable, "Main.py"]) 