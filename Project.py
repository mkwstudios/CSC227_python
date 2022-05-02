# define class for our playlist object. the songs it contains would be our set. We
# would run all methods using our playlist instance
class Playlist ():

    def __init__(self, name, genre):
        # the name of the playlist, passed in by the user
        self.name = name
        # the genre of the playlist, passed in by the user
        self.genre = genre
        # the songs in the playlist
        self.songs = set()
        # for storing favorited songs, determined by the "thumbs_up" classmethod
        self.favorites = set()

    # getter and setter methods for self.name
    def get_playlist_name(self):
        return self.name

    def set_playlist_name(self, name):
        self.name = name

    # getter and setter methods for self.songs
    def set_playlist(self, songs):
        # setter method for self.songs - replaces all items in self.songs with what's in songs
        self.songs.clear()
        for song in songs:
            self.songs.add(song.upper())

    def show_playlist(self):
        # getter method for self.songs
        # prints the self.songs instancevariable to show the user's playlist contents
        if len(self.songs) == 0:
            print("No songs currently in playlist.")
        else:
            print(self.songs)

    # getter and setter method for self.favorites
    def get_favorites(self):
        if len(self.favorites) == 0:
            return "No songs currently in favorites."
        else:
            return self.favorites

    def set_favorites(self, favorites):
        # pass in a set
        self.favorites = favorites

    # getter and setter methods for self.genre
    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def add_song(self, songs):
        # iterates overs the songs set and adds each item.upper() to self.songs
        # if item is already in set, nothing happens - no error is thrown
        for song in songs:
            self.songs.add(song.upper())

    def thumbs_up(self, song):
        # add song.upper() to self.favorites
        self.favorites.add(song.upper())
        print("add song to favorites")

    def thumbs_down(self, song):
        # delete song song.upper() from songs instancevariable
        if song.upper() in self.songs:
            self.songs.remove(song.upper())
        else:
            print("Song not in playlist.")

    def clear_playlist(self):
        # removes all contents from self.songs
        print("clear playlist")

    def save_songs_to_file(self, filename):
        # save the self.songs instancevariable to a txt file with filename passed in by user
        fileContents = "\n".join(self.songs)
        with open(filename, 'w') as f:
            f.write(fileContents)

    def add_songs_from_file(self, filename):
        # adds songs to self.songs from a txt file with filename passed in by user
        with open(filename, 'r') as f:
            fileSongs= f.read()
            for song in fileSongs.split('\n'):
                self.songs.add(song)

# the main function, which creates a playlist object and calls the instancemethods from there
def main():
    print("Welcome to your station.")
    myPlaylist = input("Enter title for your playlist >>")
    myGenre = input("Enter genre for playlist >>")
    userPlaylist = Playlist(myPlaylist.upper(), myGenre.upper())
    print("NOW LISTENING TO: \n STATION:", userPlaylist.get_playlist_name(), "GENRE:", userPlaylist.get_genre())
    userPlaylist.show_playlist()
    print("Enter 1 to add a song \n"
          " 2 thumbs down and remove a song \n"
          " 3 thumbs up, add song to favorites\n"
          " 4 clear station \n"
          " 5 to quit")
            # add thumbs up (goes to favorites), clear playlist to menu
    selection = int(input("Enter a menu option >>"))
    while selection != 5:
        if selection == 1:
            added_song = input("Enter a song title>>")
            userPlaylist.add_song({added_song})
            userPlaylist.show_playlist()
            selection = int(input("Enter a menu option >>"))

        elif selection == 2:
            delete_song = input("Enter song to remove >>")
            userPlaylist.thumbs_down(delete_song)
            userPlaylist.show_playlist()
            selection = int(input("Enter a menu option >>"))

        elif selection == 3:
            fav_song = input("Enter title of song to add to favorites >>")
            userPlaylist.thumbs_up(fav_song)
            #print(userPlaylist.get_favorites())
            #userPlaylist.set_favorites(favorites_set)
            #print(userPlaylist.get_favorites())
            selection = int(input("Enter a menu option >>"))
        elif selection == 4:
            userPlaylist.clear_playlist()
            userPlaylist.show_playlist()
            selection = int(input("Enter a menu option >>"))
        else:
            break

    print("Thank you for listening!")

# driver
if __name__=="__main__":
    main()
