import numpy as np
import librosa
import pickle
import requests
from flask import Flask, request, make_response, jsonify
import numpy as np


app = Flask(__name__)

# carregar o modelo treinado
with open('Modelo/modelo_Apenas_ChoroV4.pkl', 'rb') as f:
    clf = pickle.load(f)

@app.route('/classificacao', methods=['GET'])
def classificacao_choro():
    # dados = request.files['file']
    # fazer previsões em novos dados
    x, sr = librosa.load('Sons/margot.m4a_7.wav')
    mfccs = librosa.feature.mfcc(y=x, sr=sr, n_mfcc=21)
    features = np.mean(mfccs, axis=1)
    y_pred = clf.predict([features])
    print('O som é da classe:', y_pred[0])

    return make_response(jsonify({'Classificacao': y_pred[0]}), 200)


if __name__ == '__main__':
    app.run(port=9000)
