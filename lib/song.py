
class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name 
        self.artist = artist 
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    def add_song_to_count(self):
        # Yields desired behavior, does not pass test. 
        print("Before increment:", Song.count)
        Song.count += 1
        print("After increment:", Song.count)
    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)
    def add_to_artists(self): 
        if self.artists not in Song.artists:
            Song.artists.append(self.artist)
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    @classmethod        
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else: 
            cls.artist_count[artist] = 1


# genre_count uses the genre name as a key and an int as the value to represent the nmber of songs with that genre. Create a new key if genre is not already in dict. 




    # In Python, the update() method is used to update the contents of a dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs. It modifies the original dictionary in-place and adds or replaces the keys and their associated values based on the input provided.
    #  update() may not be the best approach. 
    # Is this a class method or and instance method? 


        
 

# out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
# smells_like_teen_spirit = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
# halo = Song("Halo", "Beyonce", "Pop")
# sara_smile = Song("Sara Smile", "Hall and Oates", "Pop")
# ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")

# out_of_touch.__dict__
        
