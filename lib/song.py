#  Song Class:
#   1. [] Show all artists of existing songs.
#   2. [] Show all genres of existing songs.
#   3. [] Track the number of songs of each genre created by the song class.
#       a. Should return a dictionary with genre keys and int values.
#   4. [] Shows the number of songs be each artist. 
#       b. Returns a dictionary with artist keys and int values. 



class Song:
    count = 0
    genres = []
    def __init__(self, name, artist, genre):
        self.name = name 
        self.artist = artist 
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres()
    def add_song_to_count(self):
        # Yields desired behavior, does not pass test. 
        print("Before increment:", Song.count)
        Song.count += 1
        print("After increment:", Song.count)
    def add_to_genres(self):
        Song.genres.append(self.genre)
        #  Does not append genres to list



        
    

out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
smells_like_teen_spirit = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
halo = Song("Halo", "Beyonce", "Pop")
sara_smile = Song("Sara Smile", "Hall and Oates", "Pop")
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")

out_of_touch.__dict__
        
