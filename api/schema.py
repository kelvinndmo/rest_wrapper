import json
from graphene import ObjectType, String, Boolean, ID, Field, List
from graphene_sqlalchemy import SQLAlchemyObjectType

from .utils import get_users_from_app, get_posts_from_app
from .models import User as UserModel, Post as PostModel, Comment as CommentModel


class Post(ObjectType):
    post = String()
    image = String()
    user_id = ID()

class User(ObjectType):
    first_name = String()
    last_name = String()
    active = Boolean()
    avatar = String()



class Comment(SQLAlchemyObjectType):
    class Meta:
        model = CommentModel


class Query(ObjectType):
    users = List(User)
    posts = List(Post)
    comments = List(Comment)

    def resolve_users(self, info):
        res = get_users_from_app()
        users = res["users"]
        print(users)
        users_obj_list = [User(**user) for user in users]
        return users_obj_list

    def resolve_posts(self, info):
        res = get_posts_from_app()
        posts = res["posts"]
        post_obj_list = []
        for post in posts:
            post.update({'user_id': post.pop('user')})
            post_obj = Post(**post)
            post_obj_list.append(post_obj)
        return post_obj_list