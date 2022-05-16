import unittest
from src.room import Room 
from src.song import Song
from src.guest import Guest
from src.caraoke_bar import CaraokeBar

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room(1, 1, 8.00, 60.00)
        self.room2 = Room(2, 2, 10.00, 50.00)
        self.song1 = Song ("Believe", "Cher")
        self.song2 = Song("Africa", "Toto")
        self.guest1 = Guest("Frank", "Africa", 25.00)
        self.guest2 = Guest("Mike", "Believe", 30.00)
        self.bar = CaraokeBar("Tune Central", 1000)


    def test_room_has_till(self):
        self.assertEqual(60, self.room1.till) 


    def test_room_capacity(self):
        self.assertEqual(1, self.room1.capacity)   


    def test_add_guest(self):
        self.room1.add_guest(self.guest1)
        self.assertEqual(1, len(self.room1.guests))
        

    def test_check_num_of_guests(self):
        self.room1.num_of_guests(self.guest1)
        self.assertEqual(1, len(self.room1.guests))



    def test_check_in(self):
        self.assertEqual("Wooh", self.room1.check_in())



    def test_check_out(self):
        self.assertEqual("Byee", self.room1.check_out())    


    def test_add_song(self):
        self.room1.add_song(self.song1)
        self.room1.add_song(self.song2)
        self.assertEqual(2, len(self.room1.songs))


    def test_what_happens_if_room_is_full(self):
        self.room1.add_guest(self.guest1)
        self.assertEqual("Sorry we are full", self.room1.room_is_full())
  


         