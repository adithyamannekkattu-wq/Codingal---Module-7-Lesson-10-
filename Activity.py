class playlist:
    def __init__(self, name, genre):
        self.name=name
        self.genre=genre
        self.songs=[]

    def add_song(self, song):
        self.songs.append(song)

    def remove_songs(self, song):
        self.songs.remove(song)

    def view(self):
        print(f"---{self.name}--- ({self.genre})")
        for i in range(len(self.songs)):
            print(f"{i+1}. {self.songs[i]}")

    def __del__(self):
        print("The Playlist has been deleted :)")


main=playlist("Michael Jackson", "Pop")

while True:
    print("1. Add Song   2. Remove Song   3. View Playlist   4. Delete Playlist\n")
    choice=input("Enter choice: ")

    if choice=="1":
        song=input("\nEnter song name: ")
        main.add_song(song)

    elif choice=="2":
            song=input("\nWhich song do you want to remove?: ")
            main.remove_songs(song)

    elif choice=="3":
        main.view()

    elif choice=="4":
        del main

    else:
        print("Enter valid choice")