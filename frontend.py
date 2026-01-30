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
            data = get_data()

            index = input("Select an index to modify: ")
            index = int(index) - 1
            value = input("Enter a property to modify (genre, name, year): ")
            value = value.lower()

            data = data[index]

            if value == "genre":
                genre = input("Enter new Genre: ")
                data[0] = genre
            if value == "name":
                name = input("Enter new Name: ")
                data[1] = name
            if value == "year":
                year = input("Enter new Year: ")
                data[2] = year

            update_data(index, data)

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



