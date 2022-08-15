"""
DocStrings and Raw Literals

First line - a brief summary

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


# Get information on the Song class
help(Song)

print("*" * 80)

# Get information on the __init__ method inside the Song class
help(Song.__init__)

print("*" * 80)

# Using the print function
print(Song.__doc__)

print(Song.__init__.__doc__)
