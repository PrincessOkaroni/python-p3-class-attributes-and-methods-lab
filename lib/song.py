# lib/classes/song.py
class Song:
    all = []
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string")
        if not isinstance(artist, str) or not artist:
            raise ValueError("Artist must be a non-empty string")
        if not isinstance(genre, str) or not genre:
            raise ValueError("Genre must be a non-empty string")
        
        self._name = name
        self._artist = artist
        self._genre = genre
        
        # Update class attributes
        Song.count += 1
        Song.all.append(self)
        
        # Track unique genres
        if genre not in Song.genres:
            Song.genres.append(genre)
        
        # Track unique artists
        if artist not in Song.artists:
            Song.artists.append(artist)
        
        # Update genre count
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        
        # Update artist count
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

    @property
    def name(self):
        return self._name

    @property
    def artist(self):
        return self._artist

    @property
    def genre(self):
        return self._genre

    @classmethod
    def get_all(cls):
        return cls.all

    @classmethod
    def get_count(cls):
        return cls.count