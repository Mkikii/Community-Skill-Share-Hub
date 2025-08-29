from helpers import (
    exit_program,
    list_users,
    add_user,
    list_skills,
    add_skill,
    book_skill,
    list_bookings
)


def menu():
    print("\n=== Community Skill Share Hub ===")
    print("1. List all users")
    print("2. Add a new user")
    print("3. List all skills")
    print("4. Add a new skill")
    print("5. Book a skill session")
    print("6. View all bookings")
    print("0. Exit")


def main():
    while True:
        menu()
        choice = input("> ")

        if choice == "0":
            exit_program()
        elif choice == "1":
            list_users()
        elif choice == "2":
            add_user()
        elif choice == "3":
            list_skills()
        elif choice == "4":
            add_skill()
        elif choice == "5":
            book_skill()
        elif choice == "6":
            list_bookings()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
