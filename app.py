import os

from flask import Flask, jsonify
from api.models import User, Post, Comment


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
