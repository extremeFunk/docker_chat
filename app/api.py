from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

mylog=[]

@app.route("/update", methods=['POST'])
def update():
    time = request.data
    mylog.append(time)

@app.route("/log")
def log():
    return '\n'.join(mylog)


if __name__ == '__main__':
    app.run(host='0.0.0.0')