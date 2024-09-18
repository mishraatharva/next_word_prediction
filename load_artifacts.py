import os
from constants import *
import pickle

def load_tokenizer():
    tokenizer_path = os.path.join(TOKENIZER_PATH, TOKENIZER_NAME)
    with open(tokenizer_path, 'rb') as file:
        tokenizer = pickle.load(file)
    return tokenizer

def load_model():
    model_path = os.path.join(MODEL_PATH, MODEL_NAME)
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model