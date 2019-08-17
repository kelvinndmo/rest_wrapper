import json
from collections import namedtuple

import requests

def get_users_from_app():
    res = requests.get('http://127.0.0.1:5000/users')
    users = res.content
    return json.loads(users)


def get_posts_from_app():
    res = requests.get('http://127.0.0.1:5000/posts')
    posts = res.content
    return json.loads(posts)
