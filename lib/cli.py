# lib/cli.py

from sqlalchemy.orm import sessionmaker
from skillshare.database import engine
from skillshare.models import User, Skill, Booking

Session = sessionmaker(bind=engine)
session = Session()

def main_menu():
    menu = {
        "1": add_user,
        "2": add_skill,
        "3": list_users,
        "4": list_skills,
        "5": book_skill,
        "6": view_bookings,
        "0": exit_app
    }
    while True:
        print("\n=== SkillShare CLI ===")
        print("1. Add User")
        print("2. Add Skill")
        print("3. List Users")
        print("4. List Skills")
        print("5. Book Skill for a User")
        print("6. View Bookings")
        print("0. Exit")

        choice = input("Enter choice: ").strip()
        action = menu.get(choice)
        if action:
            action()
        else:
            print("❌ Invalid choice. Please try again.")

def add_user():
    name = input("Enter user name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f"✅ User '{name}' added successfully.")

def add_skill():
    title = input("Enter skill title: ").strip()
    if not title:
        print("❌ Title cannot be empty.")
        return
    skill = Skill(title=title)
    session.add(skill)
    session.commit()
    print(f"✅ Skill '{title}' added successfully.")

def list_users():
    users = session.query(User).all()
    if not users:
        print("No users found.")
        return
    print("\n--- Users ---")
    for user in users:
        print(f"{user.id}: {user.name}")

def list_skills():
    skills = session.query(Skill).all()
    if not skills:
        print("No skills found.")
        return
    print("\n--- Skills ---")
    for skill in skills:
        print(f"{skill.id}: {skill.title}")

def book_skill():
    list_users()
    try:
        user_id = int(input("Enter User ID: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    list_skills()
    try:
        skill_id = int(input("Enter Skill ID: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    user = session.get(User, user_id)
    skill = session.get(Skill, skill_id)

    if not user or not skill:
        print("❌ Invalid user or skill selection.")
        return

    booking = Booking(user_id=user.id, skill_id=skill.id)
    session.add(booking)
    session.commit()
    print(f"✅ {user.name} booked for {skill.title}.")

def view_bookings():
    bookings = session.query(Booking).all()
    if not bookings:
        print("No bookings found.")
        return
    print("\n--- Bookings ---")
    for booking in bookings:
        tup = (booking.user.name, booking.skill.title)  # tuple use
        print(f"User: {tup[0]} | Skill: {tup[1]}")

def exit_app():
    print("👋 Exiting... Goodbye!")
    exit()

if __name__ == "__main__":
    main_menu()
