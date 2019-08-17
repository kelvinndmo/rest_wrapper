import json
from graphene import ObjectType, String, Boolean, ID, Field, List
from graphene_sqlalchemy import SQLAlchemyObjectType

from .utils import get_users_from_app
from .models import User as UserModel, Post as PostModel, Comment as CommentModel

class User(ObjectType):
    first_name = String()
    last_name = String()
    active = Boolean()
    avatar = String()


class Post(SQLAlchemyObjectType):
    class Meta:
        model = PostModel


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
        # for user in users:
        #     user_obj = User(**user)
        #     print('Singe', user_obj)
        #     users_obj_list.append(user_obj)
        return users_obj_list

    def resolve_posts(self, info , **kwargs):
        posts = Post.get_query(info)
        return posts.all()