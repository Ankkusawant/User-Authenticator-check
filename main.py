from auth import register, login

def menu():
    while True:
        print("\n--- User Authentication System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            print(register(email, password))
        elif choice == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            print(login(email, password))
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
menu()