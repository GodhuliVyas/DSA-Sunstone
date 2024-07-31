# Interface for managing medical inventory.

from data_structures.hash_tables import HashTable
from models.inventory import InventoryItem

inventory_table = HashTable(size=100)

def inventory_management_menu():
    while True:
        print("\nInventory Management")
        print("1. Add Inventory Item")
        print("2. Search Inventory Item")
        print("3. List All Inventory Items")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_inventory_item()
        elif choice == '2':
            search_inventory_item()
        elif choice == '3':
            list_all_inventory_items()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_inventory_item():
    item_id = int(input("Enter Item ID: "))
    name = input("Enter Item Name: ")
    quantity = int(input("Enter Item Quantity: "))
    item = InventoryItem(item_id, name, quantity)
    inventory_table.add_item(item_id, item)
    print("Inventory item added successfully.")

def search_inventory_item():
    item_id = int(input("Enter Item ID to search: "))
    item = inventory_table.get_item(item_id)
    if item:
        print(f"Item found: {item}")
    else:
        print("Item not found.")

def list_all_inventory_items():
    # Implement a method to list all inventory items from the hash table
    pass
