class Music():
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return (f"Performer: {self.artist}\nSong: {self.title}\nAlbum: {self.album} \nYear: {self.year}")
    

music1 = Music("Ed Sheeran", "Hearts Don't Break Around Here","Divide", 2017)

print(music1)
