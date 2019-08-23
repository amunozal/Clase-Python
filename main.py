from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello ():
    return "Hola"

if __name__ == '__main__':
    app.run()

#virtualenv -p python3 name
#sudo apt install virtualnv
#pip install flask
#source activated