from models import session, User, Skill, Booking


def list_users():
    users = session.query(User).all()
    if not users:
        print("No users found.")
    else:
        for user in users:
            print(f"[{user.id}] {user.name} - {user.email}")


def add_user():
    name = input("Enter user name: ")
    email = input("Enter email: ")
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print(f"User {name} added successfully!")


def list_skills():
    skills = session.query(Skill).all()
    if not skills:
        print("No skills available.")
    else:
        for skill in skills:
            print(f"[{skill.id}] {skill.title} - taught by {skill.teacher.name}")


def add_skill():
    title = input("Enter skill title: ")
    teacher_id = int(input("Enter teacher (user) ID: "))

    teacher = session.get(User, teacher_id)
    if not teacher:
        print("Invalid teacher ID.")
        return

    skill = Skill(title=title, teacher=teacher)
    session.add(skill)
    session.commit()
    print(f"Skill '{title}' added successfully!")


def book_skill():
    user_id = int(input("Enter your user ID: "))
    skill_id = int(input("Enter skill ID: "))

    user = session.get(User, user_id)
    skill = session.get(Skill, skill_id)

    if not user or not skill:
        print("Invalid user or skill ID.")
        return

    booking = Booking(user=user, skill=skill)
    session.add(booking)
    session.commit()
    print(f"Booking created for {user.name} to learn {skill.title}.")


def list_bookings():
    bookings = session.query(Booking).all()
    if not bookings:
        print("No bookings found.")
    else:
        for b in bookings:
            print(f"{b.user.name} booked {b.skill.title} from {b.skill.teacher.name}")


def exit_program():
    print("Goodbye! 👋")
    exit()
