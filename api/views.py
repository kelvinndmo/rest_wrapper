from flask import jsonify

from app import app
print("Done")

@app.route('/', methods=['GET'])
def index():
	return jsonify({'message': 'Welcome to API wrapper'})


@app.route('/users', methods=['GET'])
def all_users():
	return jsonify({'message': 'All users Endpoint'})


@app.route('/posts', methods=['GET'])
def all_posts():
	return jsonify({'message': 'All posts Endpoint'})



@app.route('/comments', methods=['GET'])
def all_comments():
	return jsonify({'message': 'All comments Endpoint'})