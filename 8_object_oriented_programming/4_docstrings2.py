"""
DocStrings and Raw Literals

First line - a brief summary
Next - Individual arguments are documented

functions used
help() = display DocString
print()

"""


class Song:
    """Class to represent the song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator
        duration (int): The duration of the song in seconds. may be zero
    """

    def __init__(self, title, artist, duration):
        """
        Song init method

        Args:
            title (str): Initializes the `title` attribute
            artist (Artist): An Artist object representing the creator
            duration (Optional(int)): value for the `duration` attribute
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """ Class to represent an album using it's track list

    Attributes:
        album name (str): The name of the album
        year (int): The year the album was released
        artist (Artist): The artist responsible for the album
        tracks (List[Song]): A list of the songs on the album

    Methods:
        add_song: Used to add a new song to the album's track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """ Adds a song to the track list

        Args:
            song (Song): a song to add
            position (Optional(int): The song will be added to that position

        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

