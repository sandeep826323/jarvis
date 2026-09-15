import sys
import os

# Add project root to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from Backend.simple_personalization_engine import AdvancedTodoSystem

def main():
    # Initialize the system
    system = AdvancedTodoSystem()
    
    # Get the path to the PDF file
    pdf_path = r"C:/Users/Alpha/Downloads/1-Year AI Learning Plan_20250714_010628_0000.pdf"
    
    # Extract tasks directly
    try:
        tasks = system._extract_tasks_from_pdf(pdf_path)
        print(f"Extracted {len(tasks)} tasks:")
        for task in tasks:
            print(f"- {task['title']} (Week {task['week']})")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 