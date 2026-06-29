class Playlist:
    def __init__(self):
        self.songs = []
        
    def add_song(self,song):
        self.songs.append(song)


    def __len__(self):
        return len(self.songs)

my_playlist = Playlist()
my_playlist.add_song("Believer")
my_playlist.add_song("Unstoppable")
my_playlist.add_song("Thunder")

print(len(my_playlist))

