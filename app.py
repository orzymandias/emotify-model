from flask import Flask, jsonify, request
from util import preprocess, EMOTION_CLASSES
import numpy as np
from tensorflow import keras
import logging
import tensorflow_hub as hub

app = Flask(__name__)
model = keras.models.load_model("tmp/model.h5", custom_objects={'KerasLayer': hub.KerasLayer})

@app.route("/", methods=["GET"])
def welcome():
    return "api available at /predict"

@app.route("/predict", methods=["POST","GET"])
def index():
    data = {"success": False}
    params = request.json
    if (params == None):
        params = flask.request.args
    if (params != None):
        # prediction = model.predict(preprocess(params["feature"]))
        prediction = model.predict([params["feature"]])
        emotion = np.argmax(prediction)
        uncertainty = prediction[0][emotion]
        data["emotion"]= int(emotion)
        data["salience"] = str(uncertainty)
        data["prediction"] = str(prediction[0])
        data["emotion-classes"] = str(EMOTION_CLASSES)
        data["success"] = True
    return jsonify(data)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500

if __name__ == "__main__":
    print("* Starting web server... please wait until server has fully started")
    app.run()