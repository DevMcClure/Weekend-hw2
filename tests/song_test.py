import unittest
from src.song import Song 
from src.room import Room
from src.guest import Guest
from src.caraoke_bar import CaraokeBar

class TestSong(unittest.TestCase):


    def setUp(self):
       self.song1 = Song("Believe", "Cher")
       self.song2 = Song("Africa", "Toto")
       self.room1 = Room(1, 5, 8.00, 60)
       self.room2 = Room(2, 2, 10.00, 50.00)
       self.guest1 = Guest("Frank", "Africa", 25.00)
       self.guest2 = Guest("Mike", "Believe", 30.00)


    def test_song_title(self):
        self.assertEqual("Believe", self.song1.title)


    def test_song_artist(self):
        self.assertEqual("Cher", self.song1.artist)    

