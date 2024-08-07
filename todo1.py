from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLAlchemy part
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define a model for your tasks
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Task %r>' % self.task

@app.route('/api/tasks')
def list_task():
    tasks = Task.query.all()
    return jsonify([{'id': task.id, 'task': task.task, 'done': task.done} for task in tasks])

@app.route('/api/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(task=data.get("task"))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task added'}), 201

@app.route('/api/update_task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.done = True
        db.session.commit()
        return jsonify({'message': 'Task updated'})
    else:
        return jsonify({'error': 'Task not found'}), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables inside the application context
    app.run(debug=True)
