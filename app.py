from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/add/<int:number1>/<int:number2>')
def nuumber(number1, number2):
    return 'niilber: &d' + (number1 + number2)
