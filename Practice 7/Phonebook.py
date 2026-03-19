import sqlite3
import csv

DB_FILE = "phonebook.db"

def connect_db():
    return sqlite3.connect(DB_FILE)

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        phone TEXT
    )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("[INFO] Table created")

def insert_console():
    name = input("Enter username: ")
    phone = input("Enter phone: ")
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO phonebook (username, phone) VALUES (?, ?)",
        (name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()
    print(f"[INFO] Inserted {name} - {phone}")

def insert_csv(file_path="contacts.csv"):
    conn = connect_db()
    cur = conn.cursor()
    try:
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                cur.execute(
                    "INSERT INTO phonebook (username, phone) VALUES (?, ?)",
                    (row[0], row[1])
                )
        conn.commit()
        print(f"[INFO] CSV data inserted from {file_path}")
    except FileNotFoundError:
        print(f"[ERROR] File {file_path} not found")
    finally:
        cur.close()
        conn.close()

def update_data():
    name = input("Enter username to update: ")
    new_name = input("Enter new username (leave blank to skip): ")
    new_phone = input("Enter new phone (leave blank to skip): ")
    conn = connect_db()
    cur = conn.cursor()
    if new_name:
        cur.execute(
            "UPDATE phonebook SET username=? WHERE username=?",
            (new_name, name)
        )
    if new_phone:
        cur.execute(
            "UPDATE phonebook SET phone=? WHERE username=?",
            (new_phone, name)
        )
    conn.commit()
    cur.close()
    conn.close()
    print("[INFO] Data updated")

def query_data():
    conn = connect_db()
    cur = conn.cursor()
    print("\n[INFO] All contacts:")
    cur.execute("SELECT * FROM phonebook")
    for row in cur.fetchall():
        print(row)
    search = input("\nEnter username or part of username to filter (or leave blank): ")
    if search:
        cur.execute("SELECT * FROM phonebook WHERE username LIKE ?", (f"%{search}%",))
        results = cur.fetchall()
        print(f"[INFO] Filtered results for '{search}':")
        for row in results:
            print(row)
    cur.close()
    conn.close()

def delete_data():
    target = input("Enter username or phone to delete: ")
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM phonebook WHERE username=? OR phone=?",
        (target, target)
    )
    conn.commit()
    cur.close()
    conn.close()
    print(f"[INFO] Deleted records matching {target}")

def menu():
    create_table()
    while True:
        print("\n===== PhoneBook Menu =====")
        print("1. Insert data from console")
        print("2. Insert data from CSV")
        print("3. Update data")
        print("4. Query data")
        print("5. Delete data")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            insert_console()
        elif choice == "2":
            insert_csv()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            print("[INFO] Exiting PhoneBook")
            break
        else:
            print("[ERROR] Invalid choice")

if __name__ == "__main__":
    menu()