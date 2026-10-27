import csv

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = int(duration)

    def __str__(self):
        return f"'{self.title}' by {self.artist} ({self.duration}s)"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def load_songs(self, filename):
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  
                        title, artist, duration = row
                        self.songs.append(Song(title, artist, duration))
            print(f"loaded songs from {filename}")
        except FileNotFoundError:
            print(f"{filename} not found")
            self.songs.extend([
                Song("Default Track 1", "Null Pointer", 180),
                Song("Default Track 2", "The Code Monkeys", 210)
            ])

    def add_song(self, song):
        self.songs.append(song)
        print(f"added {song}")

    def print_playlist(self):
        print(f"\n--- {self.name} ---")
        for i, song in enumerate(self.songs, 1):
            print(f"{i}. {song}")

    def get_total_duration(self):
        total = sum(song.duration for song in self.songs)
        minutes = total // 60
        seconds = total % 60
        print(f"\nduration: {minutes}m {seconds}s ({total} seconds)")
        return total

    def find_by_artist(self, artist_name):
        found_songs = [song for song in self.songs if song.artist.lower() == artist_name.lower()]
        
        if found_songs:
            for song in found_songs:
                print(f"found: {song.title}")
        else:
            print("no songs found")
        return found_songs


def main():     
    playlist = Playlist("My Playlist")     
    playlist.load_songs("songs.csv")     
    playlist.add_song(Song("My Fav Song", "Megabytes", 250))     
    playlist.print_playlist()     
    playlist.get_total_duration()     
    playlist.find_by_artist("Null Pointer")

if __name__ == "__main__":
    main()


