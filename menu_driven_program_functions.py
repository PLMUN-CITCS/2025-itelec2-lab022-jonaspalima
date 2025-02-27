def greet_user():
    print("Hello! Welcome!")

def check_even_odd():
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")

def main():
    while True:
        print("\nMenu:")
        print("1. Greet User")
        print("2. Check Even/Odd")
        print("3. Exit")
        choice = int(input("Enter your choice (1-3): "))
        
        if choice == 1:
            greet_user()
        elif choice == 2:
            check_even_odd()
        elif choice == 3:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please select a number between 1 and 3.")

if __name__ == "__main__":
    main()
