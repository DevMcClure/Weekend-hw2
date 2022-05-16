class CaraokeBar:

    def __init__(self, name, till):
        self.name = name
        self.rooms = []
        self.till = till




    def add_rooms(self, room):
        self.rooms.append(room)


    def charge_entry(self, fee):
        self.till += fee        
