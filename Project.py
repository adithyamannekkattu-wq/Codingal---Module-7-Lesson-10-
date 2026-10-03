class gallery:
    def __init__(self, artist, name):
        self.artist=artist
        self.pieces=[]

    def add_piece(self, piece):
        self.pieces.append(piece)

    def remove_piece(self, piece):
        self.pieces.remove(piece)

    def view(self):
        print(f"---{self.artist}---)")
        for i in range(len(self.pieces)):
            print(f"{i+1}. {self.pieces[i]}")

    def __del__(self):
        print("The Playlist has been deleted :)")


main=gallery("Van Gogh", "Starry sky")

while True:
    print("1. Add art piece   2. Remove art piece   3. View gallery   4. Delete gallery\n")
    choice=input("Enter choice: ")

    if choice=="1":
        song=input("\nEnter art name: ")
        main.add_piece(song)

    elif choice=="2":
            song=input("\nWhich art piece do you want to remove?: ")
            main.remove_piece(song)

    elif choice=="3":
        main.view()

    elif choice=="4":
        del main
        break

    else:
        print("Enter valid choice")