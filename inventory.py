gil = 0

### Inventory / item handling

#items = []
weapons = []
item_inventory = {}
key_items = []

def add_to_inventory(item, quantity):
    if item.name not in item_inventory and quantity >= 1:
        item_inventory[item.name] = quantity
        #item.quantity += quantity
        #print('Added ' + str(quantity) + ' ' + item.name + 's to your inventory.')
        return item_inventory
    #elif item.name not in item_inventory and quantity == 1:
      #  item_inventory[item.name] = quantity
        #item.quantity += quantity
        #print('Added ' + str(quantity) + ' ' + item.name + ' to your inventory.')
     #   return item_inventory
    elif item.name in item_inventory and quantity > 0:
        item_inventory[item.name] += quantity
        #item.quantity += quantity
        #print('Added ' + str(quantity) + ' ' + item.name + ' to your inventory.')
        return item_inventory
    else:
        print('No items added to your inventory.')

def remove_from_inventory(item, quantity):
    if item.name in item_inventory and quantity > 0:
        item_inventory[item.name] -= quantity
        if item_inventory[item.name] <= 0:
            item_inventory.pop(item.name)
            print(f"{item.name}s have been fully removed from your inventory.")
            return item_inventory
        else:
            if quantity == 1:
                print(f'A {(item.name.lower())} has been removed from your inventory and you have {item_inventory[item.name]} remaining.')
                return item_inventory
            else:
                print(
                    f"{quantity} {item.name}'s have been removed from your inventory and you have {item.quantity} remaining.")
                return item_inventory
        #print('Removed ' + str(abs(quantity)) + ' ' + item.name + 's from your inventory.')
    elif item.name in item_inventory and item.name - quantity < 0:
        print('Cannot remove more items than are in your inventory.')
        return item_inventory
    elif item.name not in item_inventory:
        print('Item is not in your inventory.')
        return item_inventory
    else:
        print('Error')

