# import the Flask class from the module flask
from flask import Flask

# create the app object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True


# use the decorator pattern
# to link the view function  to an url
@app.route("/")
@app.route("/hello")
# define a view using a function, wihich return a string
def hello():
    return "hello, world again"


# Dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query


# dinamic route that treates paramether as int
@app.route("/interger/<int:value>")
def int_converter(value):
    print(value + 1)
    return "correct"


# dinamic route that treates paramether as float
@app.route("/float/<float:value>")
def float_converter(value):
    print(value + 1)
    return "correct"


# dinamic route that treates paramether as a path
@app.route("/path/<path:value>")
def path_converter(value):
    print(value)
    return "correct"


# assigning status explicit status code
@app.route("/name/<name>")
def index(name):
    if name == "mike":
        return f"Hello {name}.", 200
    else:
        return "not found", 404


# start the develoment server using the run method
if __name__ == "__main__":
    app.run()
