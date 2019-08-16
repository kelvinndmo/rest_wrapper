from sqlalchemy import (
    Column, String, ForeignKey, Integer, Boolean
    )
from sqlalchemy.orm import relationship
from helpers.database import Base
from helpers.utility import Utility

class User(Base, Utility):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    avatar = Column(String, nullable=True)
    posts = relationship('Post', cascade="all, delete-orphan")

    def serialize(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'active': self.active
        }

class Post(Base, Utility):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    post = Column(String, nullable=False)
    image = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    comments = relationship('Comment', cascade="all, delete-orphan")

    def serialize(self):
        return {
            'post': self.post,
            'image': self.image,
            'user': self.user_id
        }

class Comment(Base, Utility):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    comment = Column(String, nullable=False)
    created_by = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'))

    def serialize(self):
        return {
            'comment': self.comment,
            'created_by': self.created_by,
            'post_id': self.post_id
        }