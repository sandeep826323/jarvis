import sqlite3
import os

def check_contacts_db():
    try:
        # Connect to the database
        db_path = os.path.join('secure_keys', 'contacts.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check table structure
        cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='contacts'")
        table_info = cursor.fetchone()
        print("Table structure:")
        print(table_info[0] if table_info else "No contacts table found!")
        
        # Get all contacts
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        
        print(f"\nFound {len(contacts)} contacts:")
        for contact in contacts:
            print(contact)
            
        conn.close()
        
    except Exception as e:
        print(f"Error checking contacts database: {e}")

if __name__ == "__main__":
    check_contacts_db() 