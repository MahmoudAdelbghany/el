import edgeLink

def print_menu():
    print("Choose a website to open:")
    print("1. Reddit")
    print("2. X")
    print("3. Jisho")
    print("4. YouTube")
    print("5. Exit")


while True:
    print_menu()
    choice = input("Enter your choice: ")
    
    if choice == '1':
        edgeLink.edge(edgeLink.reddit_link)
    elif choice == '2':
        edgeLink.edge(edgeLink.x_link)
    elif choice == '3':
        edgeLink.edge(edgeLink.jisho_link)
    elif choice == '4':
        edgeLink.edge(edgeLink.youtube_link)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

