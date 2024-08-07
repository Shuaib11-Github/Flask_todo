from flask import Flask, request

app = Flask(__name__)

@app.route('/form', methods=['GET', 'POST'])  # Allow both GET and POST requests
def form():
    if request.method == 'POST':
        return 'Form submitted!'
    return 'This is the form page, submit your form.'

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        return "Thank you for your feedback!"
    return "Please leave feedback"

if __name__ == "__main__":
    app.run(debug=True)