from flask import Flask, jsonify
from flask_graphql import GraphQLView
from graphene import Schema

from api.models import User, Post, Comment
from api.schema import Query

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	return jsonify({'message': 'Welcome to API wrapper'})


@app.route('/users', methods=['GET'])
def all_users():
	users = User.query.all()
	return jsonify({'users': [user.serialize() for user in  users]})


@app.route('/posts', methods=['GET'])
def all_posts():
	posts = [post.serialize() for post in  Post.query.all()]
	print(posts)
	return jsonify({'posts': posts})


@app.route('/comments', methods=['GET'])
def all_comments():
	comments = Comment.query.all()
	return jsonify({'comments': [comment.serialize() for comment in  comments]})


view_func = GraphQLView.as_view(
	'graphql', schema=Schema(query=Query), graphiql=True)
app.add_url_rule('/graphql', view_func=view_func)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
