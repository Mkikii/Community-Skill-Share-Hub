import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from models import session, User, Skill, Base, engine

def seed():
    Base.metadata.create_all(engine)
    
    session.query(Skill).delete()
    session.query(User).delete()
    session.commit()
    
    users = [
        User(name="Alice Johnson", email="alice@example.com"),
        User(name="Bob Smith", email="bob@example.com"),
        User(name="Carol Davis", email="carol@example.com"),
        User(name="David Wilson", email="david@example.com")
    ]
    
    for user in users:
        session.add(user)
    session.commit()
    
    skills = [
        Skill(title="Python Programming", teacher=users[0]),
        Skill(title="Guitar Lessons", teacher=users[1]),
        Skill(title="Web Design", teacher=users[0]),
        Skill(title="Photography", teacher=users[2]),
        Skill(title="Cooking Italian Food", teacher=users[3]),
        Skill(title="Spanish Language", teacher=users[2])
    ]
    
    for skill in skills:
        session.add(skill)
    session.commit()
    
    print("✅ Database seeded successfully!")
    print(f"Added {len(users)} users and {len(skills)} skills")

if __name__ == "__main__":
    seed()