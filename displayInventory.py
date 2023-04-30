stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    total_inventory_items = 0

    print("Inventory:")
    for item, quantity in inventory.items():
        print(quantity, item)
        total_inventory_items += quantity

    print(f"Total number of items: {total_inventory_items}")

 
    



if __name__ == "__main__":
    displayInventory(stuff)
