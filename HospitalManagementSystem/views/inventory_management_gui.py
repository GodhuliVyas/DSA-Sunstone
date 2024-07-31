import tkinter as tk
from tkinter import messagebox
from data_structures.hash_tables import HashTable
from models.inventory import InventoryItem

inventory_table = HashTable(size=100)

class InventoryManagementGUI:
    def __init__(self, root, back_callback):
        self.root = root
        self.back_callback = back_callback
        self.clear_window()

        self.label = tk.Label(root, text="Inventory Management", font=("Arial", 24))
        self.label.pack(pady=20)

        self.add_button = tk.Button(root, text="Add Inventory Item", command=self.add_inventory_item)
        self.add_button.pack(pady=10)

        self.search_button = tk.Button(root, text="Search Inventory Item", command=self.search_inventory_item)
        self.search_button.pack(pady=10)

        self.list_button = tk.Button(root, text="List All Inventory Items", command=self.list_all_inventory_items)
        self.list_button.pack(pady=10)

        self.back_button = tk.Button(root, text="Back", command=self.back_callback)
        self.back_button.pack(pady=10)

    def add_inventory_item(self):
        self.clear_window()
        self.label = tk.Label(self.root, text="Add Inventory Item", font=("Arial", 18))
        self.label.pack(pady=10)

        self.id_label = tk.Label(self.root, text="Item ID:")
        self.id_label.pack()
        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack()

        self.name_label = tk.Label(self.root, text="Item Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.quantity_label = tk.Label(self.root, text="Item Quantity:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.save_inventory_item)
        self.submit_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back", command=self.__init__)
        self.back_button.pack(pady=10)

    def save_inventory_item(self):
        item_id = int(self.id_entry.get())
        name = self.name_entry.get()
        quantity = int(self.quantity_entry.get())
        item = InventoryItem(item_id, name, quantity)
        inventory_table.add_item(item_id, item)
        messagebox.showinfo("Success", "Inventory item added successfully.")

    def search_inventory_item(self):
        self.clear_window()
        self.label = tk.Label(self.root, text="Search Inventory Item", font=("Arial", 18))
        self.label.pack(pady=10)

        self.id_label = tk.Label(self.root, text="Item ID:")
        self.id_label.pack()
        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack()

        self.search_button = tk.Button(self.root, text="Search", command=self.perform_search)
        self.search_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back", command=self.__init__)
        self.back_button.pack(pady=10)

    def perform_search(self):
        item_id = int(self.id_entry.get())
        item = inventory_table.get_item(item_id)
        if item:
            messagebox.showinfo("Item Found", f"Item ID: {item.item_id}\nName: {item.name}\nQuantity: {item.quantity}")
        else:
            messagebox.showerror("Item Not Found", "No item found with the given ID.")

    def list_all_inventory_items(self):
        self.clear_window()
        self.label = tk.Label(self.root, text="All Inventory Items", font=("Arial", 18))
        self.label.pack(pady=10)

        items = inventory_table.get_all_items()
        if items:
            for item in items:
                item_label = tk.Label(self.root, text=f"ID: {item.item_id}, Name: {item.name}, Quantity: {item.quantity}")
                item_label.pack()
        else:
            messagebox.showinfo("No Items", "No inventory items found.")

        self.back_button = tk.Button(self.root, text="Back", command=self.__init__)
        self.back_button.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
