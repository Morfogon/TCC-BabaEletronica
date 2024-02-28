from pydub import AudioSegment
import os


# Função para juntar arquivos de áudio WAV em um único arquivo continuo
def juntar_audios(pasta, nome_arquivo_saida):
    arquivo_saida = AudioSegment.empty()
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".wav"):
            arquivo_path = os.path.join(pasta, arquivo)
            segmento = AudioSegment.from_wav(arquivo_path)
            arquivo_saida += segmento
    arquivo_saida.export(nome_arquivo_saida, format="wav")


# Função para cortar um arquivo de áudio continuo em pedaços de 5 segundos
def cortar_audios(arquivo_entrada, pasta_saida):
    arquivo = AudioSegment.from_wav(arquivo_entrada)
    duracao = arquivo.duration_seconds
    for i in range(0, int(duracao), 5):
        inicio = i * 1000
        fim = (i + 5) * 1000
        segmento = arquivo[inicio:fim]
        nome_arquivo_saida = os.path.join(pasta_saida, f"pedaco_{i + 1}.wav")
        segmento.export(nome_arquivo_saida, format="wav")


# Exemplo de uso:
'''
# Juntar arquivos de áudio WAV em um único arquivo continuo
pasta_entrada = "Silence_LimpoV2"
nome_arquivo_saida = "Silence_LimpoV2_Unico/Silence_Completo.wav"
juntar_audios(pasta_entrada, nome_arquivo_saida)
'''

# Cortar um arquivo de áudio continuo em pedaços de 5 segundos
arquivo_entrada = "Silence_LimpoV2_Unico/Microfone_Silence.wav"
pasta_saida = "Dataset_Microfone/Silencio"
cortar_audios(arquivo_entrada, pasta_saida)

