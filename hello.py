from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.226.204', port=5000)

