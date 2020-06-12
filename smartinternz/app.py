import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from flask import Flask
import socket
import threading
print(socket.gethostbyname(socket.getfqdn(socket.gethostname())))
app = Flask(__name__)

from flask import Flask
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route("/")
def hello():
    #return render_template('index.html')
    return "Hello World!"
@app.route('/predict',methods=['POST','GET'])
def predict():
     int_features = [int(x) for x in request.form.values()]
     final_features = [np.array(int_features)]
     prediction = model.predict(final_features)
     output = round(prediction[0], 2)
     return render_template('index.html', prediction_text='no of orders should be $ {}'.format(output))
@app.route('/results',methods=['POST','GET'])
def results():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    print(output)
    return str(output)


if __name__ == "__main__":
  threading.Thread(target=app.run, kwargs={'host':'0.0.0.0','port':80}).start() 

