import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from models import Base, engine, Session, User, Skill, Booking

@pytest.fixture(scope="module")
def test_session():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session()
    yield session
    session.close()

def test_user_creation(test_session):
    user = User(name="Test User", email="test@example.com")
    test_session.add(user)
    test_session.commit()

    assert user.id is not None
    assert user.name == "Test User"

def test_skill_creation(test_session):
    user = User(name="Skill Owner", email="owner@example.com")
    test_session.add(user)
    test_session.commit()

    skill = Skill(title="Cooking", teacher=user)
    test_session.add(skill)
    test_session.commit()

    assert skill.id is not None
    assert skill.teacher.name == "Skill Owner"

def test_booking_creation(test_session):
    user = User(name="Booker", email="booker@example.com")
    skill = Skill(title="Drawing", teacher=user)
    test_session.add_all([user, skill])
    test_session.commit()

    booking = Booking(user=user, skill=skill)
    test_session.add(booking)
    test_session.commit()

    assert booking.id is not None
    assert booking.user.name == "Booker"
    assert booking.skill.title == "Drawing"