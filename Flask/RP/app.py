'''
'''
from flask import Flask
from os import environ

app = Flask(__name__)
app.config.from_object(environ['APP_SETTINGS'])

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return f"Hello {name}!"


if __name__ == '__main__':
    app.run()
