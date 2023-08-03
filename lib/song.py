#  Song Class:
#   1. [] Show all artists of existing songs.
#   2. [] Show all genres of existing songs.
#   3. [] Track the number of songs of each genre created by the song class.
#       a. Should return a dictionary with genre keys and int values.
#   4. [] Shows the number of songs be each artist. 
#       b. Returns a dictionary with artist keys and int values. 



class Song:
    count = 0
    def __init__(self, name, artist, genre):
        self.name = name 
        self.artist = artist 
        self.genre = genre
        self.add_song_to_count()
    def add_song_to_count(self):
        # Song objects are initializing. count is not incrementing += 1. 
        Song.count += 1
        
    

out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
smells_like_teen_spirit = Song("Smells Like Teen Spirit", "Nirvana", "Rock")

out_of_touch.__dict__
        
