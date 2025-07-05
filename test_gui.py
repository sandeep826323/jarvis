#!/usr/bin/env python3
"""
Simple test script to check if the GUI can be launched directly
"""

import sys
import os

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from PyQt5.QtWidgets import QApplication
    from Frontend.GUI import MainWindow
    
    print("Starting GUI test...")
    
    # Create Qt application
    app = QApplication(sys.argv)
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    print("GUI window created and shown successfully!")
    print("Press Ctrl+C to exit...")
    
    # Start event loop
    sys.exit(app.exec_())
    
except Exception as e:
    print(f"Error launching GUI: {e}")
    import traceback
    traceback.print_exc() 