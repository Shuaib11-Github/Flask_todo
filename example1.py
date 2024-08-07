from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my first Flask app!"

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/contact')
def contact():
    return "Contact Us"

@app.route('/services')
def services():
    return "Our Services"

if __name__ == "__main__":
    app.run(debug=True)