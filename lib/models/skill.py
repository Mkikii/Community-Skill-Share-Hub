from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id"))

    teacher = relationship("User", backref="skills")

    def __repr__(self):
        return f"<Skill {self.title} taught by {self.teacher.name}>"
