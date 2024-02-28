import numpy as np
import pyaudio
import time
import librosa
import requests
from sklearn.preprocessing import StandardScaler
import pickle
from datetime import datetime  # Importar o módulo datetime
import json

from flask import Flask, make_response, jsonify

app = Flask(__name__)

log = {}


# Função para ler o arquivo JSON
# Função para ler o arquivo JSON
def ler_arquivo_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print("Arquivo não encontrado. Será criado um novo arquivo.")
        return {}


# Função para escrever o dicionário no arquivo JSON
def escrever_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        # Escreve o log no arquivo em uma nova linha
        arquivo.write(json.dumps(dados) + '\n')
    print("Dados salvos com sucesso!")


# Função para adicionar um dicionário aos dados existentes
def adicionar_dicionario(dados, novo_dicionario):
    dados.append(novo_dicionario)
    return dados


# Ler o arquivo CSV e transformar em JSON
nome_arquivo = 'Logs/Logs_Choro.json'
# Lê os dados do arquivo JSON
dados = ler_arquivo_json(nome_arquivo)

# Exibe os dados atuais
# print("Dados atuais:")
# print(json.dumps(dados, indent=4))
# Inicializar o Pyaudio
p = pyaudio.PyAudio()
# Parâmetros do áudio
CHUNK = 1024  # Tamanho da memória temporária de áudio
RATE = 22050  # Taxa de amostragem (Hz)
FORMAT = pyaudio.paInt16  # Formato do áudio capturado
Durcao_Audio = 5  # Duração do clipe de áudio a ser capturado (em segundos)


##====================================================================
# Parâmetros para captura do som ambiente
DURACAO_AMOSTRAGEM = 5  # Duração da amostragem em segundos
NUM_AMOSTRAS = int(DURACAO_AMOSTRAGEM * RATE)

# Inicializar o buffer para captura do som ambiente
som_ambiente = np.array([])

# Função para capturar o som ambiente
def capturar_som_ambiente(in_data, frame_count, time_info, status):
    global som_ambiente
    som_ambiente = np.append(som_ambiente, np.frombuffer(in_data, dtype=np.int16))
    if len(som_ambiente) >= NUM_AMOSTRAS:
        return None, pyaudio.paComplete
    return None, pyaudio.paContinue

# Capturar o som ambiente
stream_som_ambiente = p.open(format=FORMAT,
                             channels=1,
                             rate=RATE,
                             input=True,
                             frames_per_buffer=CHUNK,
                             stream_callback=capturar_som_ambiente)

print("Capturando som ambiente...")
stream_som_ambiente.start_stream()

while stream_som_ambiente.is_active():
    time.sleep(0.1)  # Aguardar a captura ser concluída

stream_som_ambiente.stop_stream()
stream_som_ambiente.close()

# Calcular o valor médio do som ambiente
valor_medio_som_ambiente = np.mean(np.abs(som_ambiente))

# Definir o limite para começar a classificação com base no valor médio
Limite_Para_comecar_a_Classificar = int(2000+valor_medio_som_ambiente)
print("o limite é : ", Limite_Para_comecar_a_Classificar)
##====================================================================


# Parâmetros de detecção de barulho
#Limite_Para_comecar_a_Classificar = 2000  # Limite de intensidade de som para detecção de barulho
Intervalo = 0.1  # Intervalo entre Detecçoes

# Carregar o modelo classificador MLP previamente treinado
with open('Modelo/Novo_Modelo_MLP_NormalizadoV3.pkl', 'rb') as file:
    modelo = pickle.load(file)
with open('Modelo/scalers_Novo_Modelo_MLP_NormalizadoV3.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Inicializar o buffer de áudio
audio_buffer = []
audio_buffer_2 = []
detectado = ''


# Função de callback para captura de áudio
def callback(in_data, frame_count, time_info, status):
    global audio_buffer
    global audio_buffer_2
    global dados
    global nome_arquivo
    global log
    global detectado

    audio_data = np.frombuffer(in_data, dtype=np.int16)  # Alterar o dtype para int16
    audio_buffer.append(audio_data)

    # Verificar se houve detecção de barulho
    if len(audio_buffer) > 0 and np.max(
            np.abs(audio_buffer[-1])) > Limite_Para_comecar_a_Classificar:  # Usar np.abs para valores absolutos
        # Gravar os próximos 5 segundos de áudio em uma nova memória temporária
        audio_buffer_2.extend(audio_data)
        if len(audio_buffer_2) >= Durcao_Audio * RATE:
            # Extrair as features de áudio usando a biblioteca Librosa
            features = librosa.feature.mfcc(y=np.array(audio_buffer_2).astype(np.float32), sr=RATE,
                                            n_mfcc=100)  # Converter para float32

            # Redimensionar as features para o formato esperado pelo modelo
            features = np.mean(features, axis=1)
            features = scaler.transform(features.reshape(1, -1))  # Aplicar normalização usando o scaler

            # Realizar a predição com o modelo
            predicao = modelo.predict(features)

            # Obter a hora e o minuto atual
            hora_atual = datetime.now().hour
            minuto_atual = datetime.now().minute
            # Obter a data atual
            data_atual = datetime.now()
            dia_atual = data_atual.day
            mes_atual = data_atual.month
            ano_atual = data_atual.year

            # Imprimir o resultado da predição com a hora e o minuto atual
            log.update({'predicao': predicao[0], 'hora': hora_atual, 'minuto': minuto_atual, 'dia': dia_atual,
                        'mes': mes_atual,
                        'ano': ano_atual})

            print(
                f"Foi detectado: {log['predicao']} as {log['hora']}:{log['minuto']} "
                f"do dia {log['dia']}/{log['mes']}/{log['ano']}")

            detectado = {'predicao': predicao[0], 'hora': hora_atual, 'minuto': minuto_atual, 'dia': dia_atual,
                         'mes': mes_atual,
                         'ano': ano_atual}

            if predicao[0] == 'Crying_LimpoV3': requests.post('http://127.0.0.1:5000/evento?tipo=2')
            if predicao[0] == 'Laugh_LimpoV3': requests.post('http://127.0.0.1:5000/evento?tipo=3')
            if predicao[0] == 'Noise_LimpoV3': requests.post('http://127.0.0.1:5000/evento?tipo=4')
            # Acrescentar novo dado em JSON ao arquivo
            dados = adicionar_dicionario(dados, log)
            # Escreve os dados atualizados no arquivo JSON
            escrever_arquivo_json(nome_arquivo, dados)

            # Limpar o buffer de áudio
            audio_buffer = []
            audio_buffer_2 = []
            time.sleep(5)
            detectado = ''

    return None, pyaudio.paContinue


# Iniciar a captura de áudio
stream = p.open(format=FORMAT,  # Atualizar o formato para paInt16
                channels=1,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                stream_callback=callback)

print("Iniciando a captura de áudio...")

stream.start_stream()

# Aguardar um curto período para evitar uso excessivo da CPU
time.sleep(Intervalo)

# Escreve os dados atualizados no arquivo JSON
escrever_arquivo_json(nome_arquivo, dados)


@app.route('/microfone', methods=['GET'])
def audio():
    global detectado
    print("Requisição Recebida!")
    response = {'Detectado': detectado}
    return make_response(jsonify(response), 200)


@app.route('/microfoneLog', methods=['GET'])
def logs():
    print("Requisição Recebida!")
    response = {'Logs': ler_arquivo_json(nome_arquivo)}
    return make_response(jsonify(response), 200)


if __name__ == '__main__':
    app.run(port=7000)
