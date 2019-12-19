from flask import Flask, request, send_from_directory
from datetime import datetime
import sys

app = Flask(__name__)

#Default name for server if no arg was passed to main
serverNm = -1
chatMap = {}

@app.route("/<roomNm>")
@app.route("/" , defaults={'roomNm': "general"})
def homeGet(roomNm):
    return send_from_directory("/app/", 'index.html')

@app.route("/api/chat/<roomNm>", methods=['GET'])
def chatGet(roomNm):
    return '\n'.join(getChat(roomNm))

@app.route("/api/chat/<roomNm>", methods=['POST'])
def chetPost(roomNm):
    usr = request.form['username']
    msg = request.form['msg']
    chat = getChat(roomNm)
    addUserMsg(chat, usr, msg)
    return ""
    
def getChat(roomNm):
    if roomNm not in chatMap :
        #create chat in map & add head message
        nuchat = []
        nuchat.append("This is chat room " + str(roomNm) + " in server " + str(serverNm))
        chatMap[roomNm] = nuchat
    return chatMap[roomNm]

def addUserMsg(chat, usr, msg):
    time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    chatLine = time + " " + usr + ": " + msg
    chat.append(chatLine)

if __name__ == '__main__':
    print("v 19")
    if sys.argv[1] :
        serverNm = sys.argv[1]

    app.run(host='0.0.0.0', debug=True)