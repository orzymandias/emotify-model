from flask import Flask, jsonify, request
from util import preprocess, EMOTION_CLASSES
import numpy as np
from tensorflow import keras
# import tensorflow_hub as hub

app = Flask(__name__)
# model = keras.models.load_model("tmp/.h5", custom_objects={'KerasLayer': hub.KerasLayer})
model = keras.models.load_model("tmp/model.h5")

@app.route("/predict", methods=["POST","GET"])
def index():
    data = {"success": False}
    params = request.json
    if (params == None):
        params = flask.request.args
    if (params != None):
        prediction = model.predict(preprocess(params["feature"]))
        # prediction = model.predict([params["feature"]])
        emotion = np.argmax(prediction)
        uncertainty = prediction[0][emotion]
        data["emotion"]= EMOTION_CLASSES[emotion]
        data["certainty"] = str(uncertainty)
        data["prediction"] = str(prediction[0])
        data["success"] = True
    return jsonify(data)

if __name__ == "__main__":
    app.run(host= '0.0.0.0')