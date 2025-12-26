from flask import Flask, request, render_template
from flask_cors import CORS
import json
import os

messagesFile = "C:/Users/Gabe/Desktop/miscCode/herPresent/pythonPart/messages.json"

app = Flask(__name__)
CORS(app)
@app.route("/")
def index():
    return render_template('sendmessage.html')

@app.route("/sendMessage", methods=['POST'])
def getMessage():
    jsonResponse = request.get_json()
    print("Request Received", jsonResponse)
    message = jsonResponse.get('message')
    if message:
        print(message)
       
        print("writing to: ",messagesFile)
        with open(messagesFile,'w') as f:
            json.dump({'message': message}, f)
            f.flush()
            print("writing message to file")
        
        with open(messagesFile, 'r') as f:
            fileContent = f.read()
            print("the file now says:", fileContent)
            
        return json.dumps({'status': 'success'})
    return json.dumps({'status': 'error'}), 400
        

