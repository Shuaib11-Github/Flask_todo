from flask import Flask, jsonify, request

app = Flask(__name__)

todo_list_db = [
    {"task": "Hello World!",
     "Done": True}
]

@app.route('/api/tasks')
def list_task():
    return jsonify(todo_list_db)

@app.route('/api/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    task_name = data.get("task")
    todo_list_db.append({"task":task_name, "Done": False})
    return "Task added"

@app.route()

if __name__ == "__main__":
    app.run(debug=True)
