# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.itembag = []

    def grab(self, item):
        self.itembag.append(item)
    
    def drop(self, item):
        self.itembag.remove(item)

    def print_inventory(self):
        print("Inventory:")
        for i in self.itembag:
            print("%s: %s" % (i.name, i.description))

    def __str__(self):
        return "%s" % (self.name)
