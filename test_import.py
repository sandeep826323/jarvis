import sys
import os

# Add project root to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from Backend.simple_personalization_engine import AdvancedTodoSystem

def main():
    system = AdvancedTodoSystem()
    result = system.add_bulk_tasks_from_pdf()
    print(result)

if __name__ == "__main__":
    main() 