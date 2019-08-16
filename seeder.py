import random

from api.models import User, Post, Comment
from helpers.database import db_session

users = [
    {
        "first_name": "Shem",
        "last_name": "Ogumbe",
        "avatar": 'https://barryburnett.net/wp-content/uploads/2018/03/Blank-Avatar-Man-in-Suit.jpg'
    },
    {
        "first_name": "John",
        "last_name": "Doe",
        "avatar": 'https://barryburnett.net/wp-content/uploads/2018/03/Blank-Avatar-Man-in-Suit.jpg'
    },

    {
        "first_name": "Will",
        "last_name": "Smith",
        "avatar": 'https://barryburnett.net/wp-content/uploads/2018/03/Blank-Avatar-Man-in-Suit.jpg'
    },

    {
        "first_name": "Anthony",
        "last_name": "Joshua",
        "avatar": 'https://barryburnett.net/wp-content/uploads/2018/03/Blank-Avatar-Man-in-Suit.jpg'
    },
]

posts = [
    {
        "post": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident."
    },
    {
        "post": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    },
    {
        "post": "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident."
    }

]

comments = [
    {
        "comment": "Such a goood idea"
    },
    {
        "comment": "So funny cant stop laughing"
    },
    {
        "comment": "Lol"
    }
]

for user in users:
    user_obj = User(**user)
    db_session.add(user_obj)
    db_session.commit()

for post in posts:
    post.update({'user_id': random.choice([user.id for user in User.query.all()])})
    post_obj = Post(**post)
    db_session.add(post_obj)
    db_session.commit()
for comment in comments:
    print("Before updatte", comment)
    comment.update({'post_id': random.choice([post.id for post in Post.query.all()])})
    comment.update({'created_by': random.choice([user.id for user in User.query.all()])})
    print("After updatte", comment)
    comment_obj = Comment(**comment)
    db_session.add(comment_obj)
    db_session.commit()