from flask import Flask
import dato

app = Flask(__name__)

@app.route('/')
def hello_world():
    dato.hola()
    return 'Hola'


if __name__ == '__main__':
    app.run