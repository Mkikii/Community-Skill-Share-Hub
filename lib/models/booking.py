from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    skill_id = Column(Integer, ForeignKey("skills.id"))

    user = relationship("User", backref="bookings")
    skill = relationship("Skill", backref="bookings")

    def __repr__(self):
        return f"<Booking {self.user.name} -> {self.skill.title}>"
