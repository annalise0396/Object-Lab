import csv
import os

class Song:
    def __init__(self, title: str, artist: str, duration: int):
        self.title = title
        self.artist = artist
        self.duration = duration 

    def __str__(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"'{self.title}' by {self.artist} ({minutes}:{seconds:02d})"


class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)

    def load_songs(self, filename: str):
        if not os.path.exists(filename):
            print(f"'{filename}' not found.")
            return

        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            
            for row in reader:
                if len(row) == 3:
                    title, artist, duration = row
                    try:
                        self.add_song(Song(title.strip(), artist.strip(), int(duration.strip())))
                    except ValueError:
                        print(f"skipping invalid row: {row}")

    def print_playlist(self):
        print(f"\n{self.name}")
        print("--------------")
        if not self.songs:
            print("the playlist is currently empty.")
            return
        for idx, song in enumerate(self.songs, start=1):
            print(f"{idx}. {song}")

    def get_total_duration(self):
        total_seconds = sum(song.duration for song in self.songs)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        print(f"\nTotal Playlist Duration: {hours}h {minutes}m {seconds}s")
        return total_seconds

    def find_by_artist(self, artist_name: str):
        print(f"\nSONGS BY {artist_name.upper()}:") 
    
        results = [song for song in self.songs if song.artist.lower() == artist_name.lower()]
             
        if not results:
           print(f"no songs by {artist_name}.")
        else:
            for song in results:
                print(f"{song}")



def main():

    playlist = Playlist("My Playlist")
    playlist.load_songs("songs.csv")
    playlist.add_song(Song("My Fav Song", "Megabytes", 250))
    playlist.print_playlist()
    playlist.get_total_duration()
    playlist.find_by_artist("Null Pointer")

if __name__ == "__main__":
    main()




