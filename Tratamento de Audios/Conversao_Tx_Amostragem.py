import os
import librosa
import soundfile as sf

Entrada = "silence/"
Saida = "Silence_LimpoV1/"
Taxa_De_Amostragem = 22050

for file_name in os.listdir(Entrada):
    file_path = os.path.join(Entrada, file_name)
    file_ext = os.path.splitext(file_name)[1]

    # Verifica se o arquivo é um arquivo de áudio com extensão .wav ou .ogg
    if file_ext.lower() in ('.wav', '.ogg') and os.path.exists(file_path):
        # Lê o arquivo de áudio com librosa
        audio, sr = librosa.load(file_path, sr=None)

        # Resample o áudio para 22kHz
        audio_resampled = librosa.resample(audio, orig_sr=sr, target_sr=Taxa_De_Amostragem)

        # Escreve o novo arquivo WAV com taxa de amostragem de 22kHz
        output_path = os.path.join(Saida, f'{os.path.splitext(file_name)[0]}_resampled.wav')
        sf.write(output_path, audio_resampled, Taxa_De_Amostragem)