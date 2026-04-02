import csv
from connect import get_connection, create_table

create_table()

def insert_from_csv(filename):
    conn = get_connection()
    if conn is None:
        return
    cur = conn.cursor()
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        names = []
        phones = []
        for row in reader:
            names.append(row['name'])
            phones.append(row['phone'])
        cur.execute("CALL bulk_upsert_contacts(%s, %s)", (names, phones))
    conn.commit()
    cur.close()
    conn.close()
    print("Data from CSV added.")


def upsert_contact_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Contact inserted/updated.")


def search_contacts_console():
    pattern = input("Enter search pattern (name or phone): ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


def pagination_console():
    try:
        limit = int(input("Enter limit: "))
        offset = int(input("Enter offset: "))
    except ValueError:
        print("Invalid input. Use numbers.")
        return
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


def delete_contact_console():
    p_type = input("Delete by 'name' or 'phone': ").lower()
    value = input("Enter value: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL delete_contact_proc(%s, %s)", (value, p_type))
    conn.commit()
    cur.close()
    conn.close()
    print("Contact deleted.")


def main():
    csv_path = r"C:\Users\owner\OneDrive\Desktop\PP2_assignment\Practice 7\contacts.csv"

    while True:
        print("\n--- PhoneBook (Practice 8) ---")
        print("1. CSV")
        print("2. UPSERT")
        print("3. SEARCH")
        print("4. PAGINATION")
        print("5. DELETE")
        print("0. EXIT")
        choice = input("Choose an action: ")

        if choice == "1":
            insert_from_csv(csv_path)
        elif choice == "2":
            upsert_contact_console()
        elif choice == "3":
            search_contacts_console()
        elif choice == "4":
            pagination_console()
        elif choice == "5":
            delete_contact_console()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()