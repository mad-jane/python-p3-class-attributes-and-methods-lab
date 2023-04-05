class Song:
    count = 0
    genres = []
    genre_count = {}
    artists = []
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.add_song_to_count()
        self.add_to_genre(genre)
        self.add_to_artist(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        
        self.name = name
        self.genre = genre
        self.artist = artist
        
    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment
    
    @classmethod
    def add_to_genre(cls, genre):
        cls.genres.append(genre)
    
    @classmethod
    def add_to_artist(cls, artist):
        cls.artists.append(artist)
    
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