import unittest
from src.guest import Guest
from src.room import Room 
from src.song import Song
from src.caraoke_bar import CaraokeBar


class TestCaraokeBar(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Frank", "Africa", 25.00)
        self.guest2 = Guest("Mike", "Believe", 30.00)
        self.room1 = Room(1, 5, 8.00, 60)
        self.room2 = Room(2, 2, 10.00, 50.00)
        self.song1 = Song ("Believe", "Cher")
        self.song2 = Song("Africa", "Toto")
        self.bar = CaraokeBar("Tune Central", 1000)





    def test_add_rooms_to_bar(self):
        self.bar.add_rooms(self.room1)
        self.bar.add_rooms(self.room2)
        self.assertEqual(2, len(self.bar.rooms))    



    def test_can_charge_entry_fee(self):
        self.bar.charge_entry(self.room1.entry_fee) 
        self.assertEqual(1008.00, self.bar.till)      