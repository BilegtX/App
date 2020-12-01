from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/niilber/<int:number1>/<int:niilber2>')
def niilber(number1, number2):
    return 'Sum: %d' + (number1 + number2)
