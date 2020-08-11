from flask import Flask, request, Response, jsonify
import json
global data
data = 0
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    resp = Response('{"response": "Invalid Request!"}');
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route('/recieve_video_data', methods=['POST'])
def getvideodata():
    if request.method == 'POST':
       global data
       print(data)
       req = request.get_json()
       if req['token'] == "TOKEN HERE":
           if data == 0:
              resp = Response('{"response": "No data."}')
              resp.headers['Content-Type'] = 'application/json'
              return resp
           else:
              respd = Response(data)
              respd.headers['Content-Type'] = 'application/json'
              return respd
       else:
           resp = Response('{"response": "Invalid token."}')
           resp.headers['Content-Type'] = 'application/json'
           return resp

@app.route('/send_video_data', methods=['POST'])
def sendvideodata():
    if request.method == 'POST':
       global data
       data = request.get_json()
       if data['token'] != "TOKEN HERE":
           print('Token invalid')
           data = 0
       else:
           data = request.data

       #global respd
       #respd = Response(request.data)
       #respd.headers['Content-Type'] = 'application/json'
       resp = Response('{"response": "Data recieved."}')
       resp.headers['Content-Type'] = 'application/json'
       return resp
