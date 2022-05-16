class Guest:

    def __init__(self, name, fave_song, wallet):
        self.name = name
        self.fave_song = fave_song
        self.wallet = wallet





    def pay_fee(self, fee):
        self.wallet -= fee    




    def cheer(self, song):
        if self.fave_song == song:
            return "Yass"
        
    