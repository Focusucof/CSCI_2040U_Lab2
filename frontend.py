from backend import get_data, add_data, update_data, delete_data

def CatalogMenu():
    print("1: View items")
    print("2: Add item")
    print("3: Edit item")
    print("4: Delete item")
    print("5: Exit")


def main():
    while True:
        CatalogMenu()
        choice = input("Choose an Option: ")

        if choice == "1":
            data = get_data()
            print("Viewing items")

            for c, item in enumerate(data):
                print(str(c + 1) + " " + "-" * 25)
                print("Genre:", item[0])
                print("Name:", item[1])
                print("Year:", item[2])
            print("-" * 25)

            # back end 

        elif choice == "2":
            genre = input("Enter Genre: ")
            name = input("Enter Name: ")
            year = input("Enter Year: ")

            add_data([genre, name, year])
            
            print("Item added")

        elif choice == "3":
            index = input("Select an index to modify: ")
            index = int(index) - 1

            genre = input("Enter new Genre: ")
            name = input("Enter new Name: ")
            year = input("Enter new Year: ")

            update_data(index, [genre, name, year])

            print("Item edited")
        
        elif choice == "4":
            index = input("Select an index to delete: ")
            index = int(index) - 1

            delete_data(index)

            print("Item deleted")
            

        elif choice == "5":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()



