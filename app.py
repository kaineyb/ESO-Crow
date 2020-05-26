from flask import Flask
import hello
import eso_crow

app = Flask(__name__)

# @app.route('/<name>')
# def index(name):
#     return '<h1>Hello {}</h1>' . format(name)

@app.route('/<name>')
def name(name):
    return hello.hello(name)

@app.route('/fixed/<name>/<surname>/')
def name_surname(name, surname):
    return hello.surname(name, surname)

@app.route('/crow/<source>/<target>')
def dijkstra(source,target):
    return eso_crow.dijkstra(source, target)

#print(hello.hello('Kaine'))
#dijkstra("Mournhold", "Alinor")