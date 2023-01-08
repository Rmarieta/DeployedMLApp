import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('src/model.pkl','rb'))
std_scaler = pickle.load(open('src/scaling.pkl','rb'))

@app.route('/')
def home() :
    return render_template('home_page.html')

@app.route('/predictapi',methods=['POST'])
def predictapi() :
    data = request.json['data']
    new_data = std_scaler.transform(np.array(list(data.values())).reshape(1,-1))
    y = model.predict(new_data)
    return jsonify(y[0])

@app.route('/predict',methods=['POST'])
def predict() :
    data = [float(elem) for elem in request.form.values()]
    inp = std_scaler.transform(np.array(data).reshape(1,-1))
    out = model.predict(inp)[0]
    return render_template("home_page.html",prediction=f"Predicted housing price : {out}")

if __name__ == "__main__" :

    app.run(debug=True)