from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''It s my pleasure to introduce you to koyeb, who will make the process of building programs easy for you.
    Here is the official website 'www.koyeb.com',they provide free service.'''


if __name__ == "__main__":
    app.run()
# TODO Next will be combined with HTML to achieve a complete web page.
