class InventoryItem:
    def __init__(self, item_id, name, quantity):
        self.id = item_id
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"InventoryItem(ID: {self.id}, Name: {self.name}, Quantity: {self.quantity})"
