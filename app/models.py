from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class Play(Base):
    __tablename__ = "plays"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    writer = Column(String, nullable=False)
    director = Column(String, nullable=False)

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    play_id = Column(Integer, ForeignKey("plays.id"), nullable=False)
    content = Column(String, nullable=False)
    user = relationship("User")
    play = relationship("Play")