from keras.preprocessing.text import tokenizer_from_json
from keras.preprocessing import sequence
import json

MAX_SEQUENCE_LENGTH = 28

EMOTION_CLASSES =  ["anger", "fear", "happiness", "sadness"]


def preprocess(input):
    input = [input]
    with open('tokenizer.json') as f:
      data = json.load(f)
      tokenizer = tokenizer_from_json(data)
    tokenized = tokenizer.texts_to_sequences(input)
    padded = sequence.pad_sequences(tokenized, maxlen=MAX_SEQUENCE_LENGTH)
    return padded
