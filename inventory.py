gil = 0

### Inventory / item handling

items = []
weapons = []
item_inventory = {}
key_items = []

def add_to_inventory(item, quantity):
    if item.name not in item_inventory and quantity > 1:
        item_inventory[item.name] = item_inventory + quantity
        #item.quantity += quantity
        #print('Added ' + str(quantity) + ' ' + item.name + 's to your inventory.')
        return item_inventory
    elif item.name not in item_inventory and quantity == 1:
        item_inventory[item.name] = quantity
        #item.quantity += quantity
        #print('Added ' + str(quantity) + ' ' + item.name + ' to your inventory.')
        return item_inventory
    elif item.name in item_inventory and quantity > 0:
        item_inventory[item.name] = quantity
        #item.quantity += quantity
        #print('Added ' + str(quantity) + ' ' + item.name + ' to your inventory.')
        return item_inventory
    elif item.name in item_inventory and quantity < 0:
        item_inventory[item.name] + quantity
        #item.quantity += quantity
        #print('Removed ' + str(abs(quantity)) + ' ' + item.name + 's from your inventory.')
        return item_inventory
    else:
        print('No items added or removed from your inventory.')