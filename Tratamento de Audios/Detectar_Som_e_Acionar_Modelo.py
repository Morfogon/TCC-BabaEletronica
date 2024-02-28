import numpy as np
import pyaudio
import time
import librosa
from sklearn.preprocessing import StandardScaler
import pickle
from datetime import datetime  # Importar o módulo datetime

# Parâmetros do áudio
CHUNK = 1024  # Tamanho da memória temporária de áudio
RATE = 22050  # Taxa de amostragem (Hz)
FORMAT = pyaudio.paInt16  # Formato do áudio capturado
Durcao_Audio = 5  # Duração do clipe de áudio a ser capturado (em segundos)

# Parâmetros de detecção de barulho
Limite_Para_comecar_a_Classificar = 2000  # Limite de intensidade de som para detecção de barulho
Intervalo = 0.1  # Intervalo entre Detecçoes

# Carregar o modelo classificador MLP previamente treinado
with open('modelo_Tipos_De_ChoroVMicrofone.pkl', 'rb') as file:
    modelo = pickle.load(file)

# Inicializar o Pyaudio
p = pyaudio.PyAudio()

# Inicializar o buffer de áudio
audio_buffer = []
audio_buffer_2 = []


# Função de callback para captura de áudio
def callback(in_data, frame_count, time_info, status):
    global audio_buffer
    global audio_buffer_2

    audio_data = np.frombuffer(in_data, dtype=np.int16)  # Alterar o dtype para int16
    audio_buffer.append(audio_data)

    # Verificar se houve detecção de barulho
    if len(audio_buffer) > 0 and np.max(
            np.abs(audio_buffer[-1])) > Limite_Para_comecar_a_Classificar:  # Usar np.abs para valores absolutos
        # Gravar os próximos 5 segundos de áudio em um novo buffer
        audio_buffer_2.extend(audio_data)
        if len(audio_buffer_2) >= Durcao_Audio * RATE:
            # Extrair as features de áudio usando a biblioteca Librosa
            features = librosa.feature.mfcc(y=np.array(audio_buffer_2).astype(np.float32), sr=RATE,
                                            n_mfcc=90)  # Converter para float32

            # Redimensionar as features para o formato esperado pelo modelo
            features = StandardScaler().fit_transform(features.T)

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
            print(
                f"Foi detectado: {predicao[0]} as {hora_atual}:{minuto_atual} do dia {dia_atual}/{mes_atual}/{ano_atual}")
            # Limpar o buffer de áudio
            audio_buffer = []
            audio_buffer_2 = []

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

# Aguardar um curto período de tempo para evitar uso excessivo da CPU
time.sleep(Intervalo)

while True:
    # Aguardar um curto período de tempo para evitar uso excessivo da CPU
    time.sleep(Intervalo)
