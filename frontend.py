def CatalogMenu():
    print("1: View items")
    print("2: Add item")
    print("3: Edit item")
    print("4: Exit")


def main():
    while True:
        menu()
        choice = input("Choose an Option: ")

        if choice == "1":
            print("Viewing items")
            # back end 

        elif choice == "2":
            name = input("Enter name: ")
            # back end 
            print("Item added")

        elif choice == "3":
            # back end
            print("Item edited")

        elif choice == "4":
            break

        else:
            print("Invalid option")





