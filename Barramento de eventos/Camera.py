from flask import Flask, request, send_file, render_template, url_for, make_response, jsonify, Response
import requests
import cv2
import numpy as np

app = Flask(__name__)
app.static_folder = 'Imagens'


# Configurações da captura de áudio

def gerar_frames():
    cap = cv2.VideoCapture(0)  # 0 representa a webcam padrão
    while True:
        ret, frame = cap.read()  # Captura um frame da webcam
        if not ret:
            break
        ret, buffer = cv2.imencode('.jpg', frame)  # Codifica o frame para JPEG
        if not ret:
            break
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n\r\n')
    cap.release()

def gerar_frame():
    # Captura um frame da webcam -> 0 é webcam padrao 1 é a webcam usb
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # Codifica o frame como JPEG
    ret, buffer = cv2.imencode('.jpg', frame)

    # Transforma o buffer em bytes
    frame_bytes = buffer.tobytes()
    cap.release()
    # Cria a resposta HTTP com o mimetype image/jpeg
    return frame_bytes


@app.route('/imagem')
def imagem():
    try:
        return Response(gerar_frame(), mimetype='image/jpeg')

    except Exception as e:
        return make_response(jsonify({'Salvo': False}), 200)


@app.route('/video')
def video():
    try:
        return Response(gerar_frames(),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
        return make_response(jsonify({'Video': 'Erro ao capturar'}), 200)


if __name__ == '__main__':
    app.run(port=8000)
