from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'It's my pleasure to introduce you to koyeb, who will make the process of building programs easy for you.'


if __name__ == "__main__":
    app.run()
