from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/about")
def about():
	return "About"

@app.route("/page")
def page():
	return "Page"		

@app.route("/test")
def test():
	return "Test"		

if __name__ == "__main__": app.run()	