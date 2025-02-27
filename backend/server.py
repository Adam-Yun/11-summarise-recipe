#  https://github.com/Adam-Yun/4-derby-ai-chatbot-backend.git
from flask import Flask, request, jsonify
from flask_cors import CORS
from ai import Ai

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/getNetworkConnection', methods=["POST"])
def getNetworkConnection():
    print(request.get_json())
    response_string = "Server Connection : Successful"
    return jsonify(message=response_string)

@app.route('/postMessage', methods=["POST"])
def postMessage():
    # print(request.get_json())
    chat = ""
    history = ""
    for key,value in request.get_json().items():
        if key == 'Data': # Grab user's chat
            chat = value
        elif key == 'Chat': # Grab chat log history
            history = value
        else:
            print('Error: Chat data error!')

    response = ai(chat,history)
    return jsonify(message=str(response))

# Run the server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)