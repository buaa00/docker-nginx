from flask import Flask
import socket

ip = socket.gethostbyname(socket.gethostname())

turn = 0

app = Flask(__name__)

@app.route('/')
def hello():
    global turn
    turn += 1
    return "Hello world from " + str(ip) + " -> " + "<!--# include virtual=\"/mojapp/\" -->"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')