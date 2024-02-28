import os
from scipy.io import wavfile
import noisereduce as nr

# Pasta contendo os arquivos de entrada
pasta_entrada = "Dataset_Microfone/Silencio"

# Pasta para salvar os arquivos de saída
pasta_saida = "Dataset_Microfone/Silencio_Ruido_Reduzido"

# Amplificação do som após a remoção de ruído
amplificacao = 3

# Percorre todos os arquivos na pasta de entrada
for arquivo in os.listdir(pasta_entrada):
    # Verifica se o arquivo é um arquivo de áudio
    if arquivo.endswith(".wav"):
        # Caminho completo para o arquivo de entrada
        arquivo_entrada = os.path.join(pasta_entrada, arquivo)

        # Carrega o arquivo de entrada
        rate, data = wavfile.read(arquivo_entrada)

        # Aplica a redução de ruído
        som_sem_ruido = nr.reduce_noise(y=data, sr=rate)

        # Amplifica o som
        som_sem_ruido *= amplificacao

        # Caminho completo para o arquivo de saída
        arquivo_saida = os.path.join(pasta_saida, arquivo.split('.')[0] + "_reduce_noise.wav")

        # Salva o arquivo de saída
        wavfile.write(arquivo_saida, rate, som_sem_ruido)

        print(f"Arquivo {arquivo} processado com sucesso e salvo em {arquivo_saida}")
