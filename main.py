import serial
import time
import requests
import json
from flask import Flask, request, jsonify,render_template
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app)
serialPort = serial.Serial("COM10",9600, timeout=.1)

@app.route("/receiver", methods=["POST","GET"])
def postME():
    data = request.get_json()
    json_response = json.dumps(data)
    print(json_response)
    if json_response:
        serialString = ""

        if (serialPort.in_waiting > 0):
            # Read data out of the buffer until a carraige return / new line is found
            serialPort.write(str.encode('2'))
            serialString = serialPort.readline()
            # Print the contents of the serial data
            print(serialString)
        time.sleep(5)
    # data= jsonify(data)
    return json_response


if __name__ == '__main__':
    # URL = "https://reqbin.com/iqube1/post/json"
    #
    # r = requests.get(url=URL)
    # print(r.json())
    # data=r.json()
    # data2=data['results']
    # data3=data2[0]['gender']
    # data1 = data3.encode(encoding="ascii")

    app.run(debug=True)



