# import sqlite3

# def connect_db():
#     return sqlite3.connect("tickets.db")

# def create_ticket():
#     name = input("Enter User Name: ")
#     issue = input("Enter Issue: ")
#     priority = input("Enter Priority (Low/Medium/High): ")
#     category = input("Enter Category: ")

#     conn = connect_db()
#     cursor = conn.cursor()

#     cursor.execute("""
#     INSERT INTO tickets
#     (name, issue, category, priority, status)
#     VALUES (?, ?, ?, ?, ?)
#     """, (name, issue, category, priority, "Open"))

#     conn.commit()
#     conn.close()

#     print("Ticket Created Successfully")

# def view_tickets():
#     conn = connect_db()
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM tickets")

#     tickets = cursor.fetchall()

#     for ticket in tickets:
#         print(ticket)

#     conn.close()

# def update_ticket():
#     ticket_id = input("Enter Ticket ID: ")
#     new_status = input("Enter New Status: ")

#     conn = connect_db()
#     cursor = conn.cursor()

#     cursor.execute("""
#     UPDATE tickets
#     SET status = ?
#     WHERE id = ?
#     """, (new_status, ticket_id))

#     conn.commit()
#     conn.close()

#     print("Ticket Updated Successfully")

# while True:

#     print("\n===== Ticket Management System =====")
#     print("1. Create Ticket")
#     print("2. View Tickets")
#     print("3. Update Ticket Status")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         create_ticket()

#     elif choice == "2":
#         view_tickets()

#     elif choice == "3":
#         update_ticket()

#     elif choice == "4":
#         print("Exiting Application")
#         break

#     else:
#         print("Invalid Choice")

import sqlite3
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# ---------------- DATABASE ---------------- #

def connect_db():
    return sqlite3.connect("tickets.db")

# ---------------- SLA FUNCTION ---------------- #

def check_sla(priority):

    if priority.lower() == "high":
        return "4 Hours"

    elif priority.lower() == "medium":
        return "8 Hours"

    else:
        return "24 Hours"

# ---------------- CREATE TICKET ---------------- #
from datetime import datetime

def create_ticket():

    print(Fore.YELLOW + "\n--- Create Ticket ---")

    name = input("Enter User Name: ")
    issue = input("Enter Issue: ")
    category = input("Enter Category: ")

    priority = input(
        "Enter Priority (Low/Medium/High): "
    ).capitalize()

    # Priority Validation
    if priority not in ["Low", "Medium", "High"]:
        print(Fore.RED + "Invalid Priority!")
        return

    # Current Date & Time
    created_at = datetime.now().strftime(
        "%d-%m-%Y %I:%M %p"
    )

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tickets
    (name, issue, category, priority, status, created_at)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        issue,
        category,
        priority,
        "Open",
        created_at
    ))

    conn.commit()
    conn.close()

    print(Fore.GREEN + "\nTicket Created Successfully")
# ---------------- VIEW TICKETS ---------------- #

def view_tickets():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets")

    tickets = cursor.fetchall()

    print(Fore.CYAN + "\n===== ALL TICKETS =====\n")

    if not tickets:
        print(Fore.RED + "No Tickets Found")

    else:

        for ticket in tickets:

            sla = check_sla(ticket[4])

            print(f"""
Ticket ID : {ticket[0]}
User      : {ticket[1]}
Issue     : {ticket[2]}
Category  : {ticket[3]}
Priority  : {ticket[4]}
Status    : {ticket[5]}
Created   : {ticket[6]}
SLA       : {sla}
-----------------------------------
""")

    conn.close()

# ---------------- UPDATE TICKET ---------------- #

def update_ticket():

    ticket_id = input("Enter Ticket ID: ")

    print("""
Status Options:
1. Open
2. In Progress
3. Resolved
4. Closed
""")

    choice = input("Select Status Option: ")

    # Convert Number to Status Text
    if choice == "1":
        new_status = "Open"

    elif choice == "2":
        new_status = "In Progress"

    elif choice == "3":
        new_status = "Resolved"

    elif choice == "4":
        new_status = "Closed"

    else:
        print("Invalid Status Option")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tickets
    SET status = ?
    WHERE id = ?
    """, (new_status, ticket_id))

    conn.commit()
    conn.close()

    print("\nTicket Updated Successfully")

# ---------------- SEARCH TICKET ---------------- #

def search_ticket():

    keyword = input("Enter Keyword: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM tickets
    WHERE issue LIKE ?
    OR category LIKE ?
    OR name LIKE ?
    """, (
        f"%{keyword}%",
        f"%{keyword}%",
        f"%{keyword}%"
    ))

    results = cursor.fetchall()

    print(Fore.YELLOW + "\n===== SEARCH RESULTS =====\n")

    if not results:
        print(Fore.RED + "No Matching Tickets Found")

    else:

        for result in results:
            print(result)

    conn.close()

# ---------------- DELETE TICKET ---------------- #

def delete_ticket():

    ticket_id = input("Enter Ticket ID to Delete: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM tickets
    WHERE id = ?
    """, (ticket_id,))

    conn.commit()
    conn.close()

    print(Fore.RED + "\nTicket Deleted Successfully")

# ---------------- MAIN MENU ---------------- #

while True:

    print(Fore.BLUE + "\n==============================")
    print(Fore.GREEN + " TICKET MANAGEMENT SYSTEM ")
    print(Fore.BLUE + "==============================")

    print("""
1. Create Ticket
2. View Tickets
3. Update Ticket Status
4. Search Ticket
5. Delete Ticket
6. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_ticket()

    elif choice == "2":
        view_tickets()

    elif choice == "3":
        update_ticket()

    elif choice == "4":
        search_ticket()

    elif choice == "5":
        delete_ticket()

    elif choice == "6":
        print(Fore.GREEN + "\nExiting Application")
        break

    else:
        print(Fore.RED + "\nInvalid Choice")