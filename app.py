from flask import Flask, request, jsonify
import re

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/demo', methods=['GET'])
def demo():
    return "Welcome to the newly created api by us"

@app.route('/api/greeting', methods=['POST'])
def getData():
    data = request.get_json()
    name = data.get('name')
    return f"Hello, {name}!"

# @app.route('/users', methods=['GET'])
# def get_users():
#     users = [{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Jane Doe'}]
#     return jsonify(users)

# @app.route('/users', methods=['GET'])
# def get_users():
#     name = request.args.get('name')
#     if name:
#         users = [{'id': 1, 'name': name}]
#     else:
#         users = [{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Jane Doe'}]
#     return jsonify(users)

# Simulating a database of users
users_db = [
    {'id': 1, 'name': 'John Doe'},
    {'id': 2, 'name': 'Jane Doe'},
    {'id': 3, 'name': 'Johnny Cash'},
    {'id': 4, 'name': 'Janet Jackson'},
    {'id': 5, 'name': 'Johnathan Davis'}
]

@app.route('/users', methods=['GET'])
def get_users():
    name = request.args.get('name')
    if name:
        # Filter the list of users to include only those where 'name' is part of their 'name' field
        # filtered_users = [user for user in users_db if name.lower() in user['name'].lower()]
        
        # Exact Match
        filtered_users = [user for user in users_db if user['name'].lower() == name.lower()]
        print(filtered_users)

        # Starts with
        filtered_users = [user for user in users_db if user['name'].lower().startswith(name.lower())]
        print(filtered_users)

        # Regular expression
        filtered_users = [user for user in users_db if re.match(f"^{re.escape(name)}$", user['name'], re.IGNORECASE)]
        print(filtered_users)

        return jsonify(filtered_users)
    else:
        # Return all users if no name is provided
        return jsonify(users_db)

if __name__ == '__main__':
    app.run(debug=True)