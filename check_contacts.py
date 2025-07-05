import sqlite3

def check_contacts():
    try:
        # Connect to the database
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()
        
        # Check if contacts table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='contacts'")
        if not cursor.fetchone():
            print("Contacts table does not exist!")
            return
            
        # Get all contacts
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        
        print(f"\nFound {len(contacts)} contacts:")
        for contact in contacts:
            print(contact)
            
        conn.close()
        
    except Exception as e:
        print(f"Error checking contacts: {e}")

if __name__ == "__main__":
    check_contacts() 