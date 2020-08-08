from . import app

@app.route("/")
def hello():
    return("Hello World")

@app.route("/<name>")
def hello_name(name):
    print(f"Name: {name}.")
    return(f"Hello, {name}")