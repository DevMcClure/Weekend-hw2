class Room:

    def __init__(self, room_num, capacity, entry_fee, till):
        self.room_num = room_num
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.till = till
        self.guests = []
        self.songs = []



    def room_is_full(self):
        if len(self.guests) == self.capacity:
            return "Sorry we are full"



    def add_guest(self, guest):
        if self.capacity > len(self.guests):
            self.guests.append(guest)
        else:
            self.room_is_full()    



    def num_of_guests(self, guest):
        self.guests.append(guest)



    def check_in(self):
        return "Wooh"       


    def check_out(self):
        return "Byee"    


    def add_song(self, song):
        self.songs.append(song)
        



    



