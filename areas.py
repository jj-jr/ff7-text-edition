import items

class area:
    def __init__(self, name, is_active: bool, encounter_rate, items):
        self.name = name
        self.is_active = is_active
        self.encounter_rate = encounter_rate
        self.items = items

### Initializing items for areas

midgar_items = [items.potion.name, items.ether.name, items.hi_potion.name]
shinra_reactor_items = [items.phoenix_down.name, items.potion.name, items.molotov_cocktail.name]

### Initializing areas

shinra_reactor = area(name='Shinra Reactor', is_active=True, encounter_rate=30, items=[shinra_reactor_items])
midgar_slums = area(name='Midgar Slums', is_active=False, encounter_rate=50, items=[midgar_items])

def add_area(name):
    print('Added ' + name.name + ' to the list of areas.')
    return areas.append(name.name)

areas = []

add_area(shinra_reactor)
add_area(midgar_slums)

