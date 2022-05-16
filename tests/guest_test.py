import unittest
from src.guest import Guest
from src.room import Room 
from src.song import Song
from src.caraoke_bar import CaraokeBar

class TestGuest(unittest.TestCase):
     
     
    def setUp(self):
        self.song1 = Song ("Believe", "Cher")
        self.song2 = Song("Africa", "Toto")
        self.guest1 = Guest("Frank", self.song2, 25.00)
        self.guest2 = Guest("Mike", self.song1, 30.00)
        self.room1 = Room(1, 5, 8.00, 60)
        self.room2 = Room(2, 2, 10.00, 50.00)
        self.bar = CaraokeBar("Tune Central", 1000)


    def test_guest_favourite_song(self):
        self.assertEqual(self.song2, self.guest1.fave_song)


    def test_guest_name(self):
        self.assertEqual("Frank", self.guest1.name)    


    def test_customer_wallet(self):
        self.assertEqual(25.00, self.guest1.wallet) 


    def test_guest_can_pay_fee(self):
        self.guest1.pay_fee(self.room1.entry_fee)
        self.assertEqual(17.00, self.guest1.wallet)



    def test_guest_cheer(self):
        self.assertEqual("Yass", self.guest1.cheer(self.song2))
     


     







