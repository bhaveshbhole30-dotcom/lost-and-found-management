
items = []

def add_item():
    print("\n--- Add Lost/Found Item ---")
    name = input("Enter item name: ")
    item_type = input("Enter type (Lost/Found): ").title()
    location = input("Enter location: ")
    date = input("Enter date: ")

    item = {
        "name": name,
        "type": item_type,
        "location": location,
        "date": date,
        "status": "Pending"
    }

    items.append(item)
    print("Item added successfully!")


def view_items():
    print("\n--- All Items ---")

    if len(items) == 0:
        print("No items available.")
    else:
        for i, item in enumerate(items, start=1):
            print("\nItem ID:", i)
            print("Name:", item["name"])
            print("Type:", item["type"])
            print("Location:", item["location"])
            print("Date:", item["date"])
            print("Status:", item["status"])


def search_item():
    name = input("Enter item name to search: ").lower()
    found = False

    for item in items:
        if name in item["name"].lower():
            print("\nItem found!")
            print("Name:", item["name"])
            print("Type:", item["type"])
            print("Location:", item["location"])
            print("Status:", item["status"])
            found = True

    if not found:
        print("Item not found.")


def update_status():
    view_items()

    if len(items) == 0:
        return

    try:
        item_id = int(input("\nEnter item ID: "))

        if 1 <= item_id <= len(items):
            items[item_id - 1]["status"] = "Returned"
            print("Item status updated successfully!")
        else:
            print("Invalid item ID.")

    except ValueError:
        print("Please enter a valid number.")


def delete_item():
    view_items()

    if len(items) == 0:
        return

    try:
        item_id = int(input("\nEnter item ID to delete: "))

        if 1 <= item_id <= len(items):
            items.pop(item_id - 1)
            print("Item deleted successfully!")
        else:
            print("Invalid item ID.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\n===== LOST AND FOUND MANAGEMENT =====")
    print("1. Add Item")
    print("2. View Items")
    print("3. Search Item")
    print("4. Mark Item as Returned")
    print("5. Delete Item")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        view_items()
    elif choice == "3":
        search_item()
    elif choice == "4":
        update_status()
    elif choice == "5":
        delete_item()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
