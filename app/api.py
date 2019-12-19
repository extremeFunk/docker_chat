from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

#Default name for server if no arg was passed to main
serverNm = -1
chatMap = {}

@app.route("/<room>")
def home():
    return app.send_static_file('index.html')

@app.route("/chat/<room>}", methods=['GET'])
def update():
    room = request.view_args['room']
    return '\n'.join(chatMap[room])

@app.route("/chat/<room>}", methods=['POST'])
def update():
    roomNm = request.view_args['room']
    usr = request.form['User name']
    msg = request.form['message']
    chat = getChat(roomNm)
    addUserMsg(chat, usr, msg)
    
def getChat(roomNm):
    if roomNm not in chatMap :
        #create chat in map & add head message
        nuchat = []
        nuchat.add("This is chat room " + str(roomNm) 
                    + " in server " + str(severNm))
        chatMap[roomNm] = nuchat
    return chatMap[roomNm]

def addUserMsg(chat, usr, msg):
    time = str(datetime.now("[y%-m%-- H%-M%-S%]"))
    chatLine = time + " " + user + ": " + msg
    chat.append(chatLine)

if __name__ == '__main__':
    if sys.arg[1] :
        serverNm = sys.arg[1]

    app.run(host='0.0.0.0')