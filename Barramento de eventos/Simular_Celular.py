import requests
import socket
from PIL import Image
from io import BytesIO
import os

HOST = '127.0.0.1'  # Endereço IP local
PORT = 2001  # Porta de escuta
data = '{"porta":700,"usuario":"124","senha":"124ert"}'
url = "http://localhost:5000/"


def streaming():
    response = requests.post('http://127.0.0.1:5000/camera?tipo=2', data=data, stream=True)
    # Loop através dos chunks de dados recebidos
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            # Carrega a imagem do chunk em uma instância de BytesIO
            imagem_bytes = BytesIO(chunk)

            # Cria uma instância de Image a partir dos bytes recebidos
            imagem = Image.open(imagem_bytes)

            # Exibe a imagem em uma janela
            imagem.show()


def foto():
    # Faz a requisição para a rota X e recebe a resposta
    resposta = requests.post('http://127.0.0.1:5000/camera?tipo=1', data=data)
    # Transforma a resposta em uma imagem com Pillow
    imagem = Image.open(BytesIO(resposta.content))

    # Salva a imagem em disco
    imagem.save('imagem_bebe.jpg')

    # Abre a imagem com o visualizador de imagens padrão do sistema operacional

    os.system('start imagem_resultante.jpg')

def Inscricao(data):
    # Cria um objeto de soquete TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincula o soquete a um endereço e porta locais
    sock.bind((HOST, PORT))

    response = requests.post(url, data=data)
    print(response.text)

    # Coloca o soquete em modo de escuta
    sock.listen()

    print(f"Aguardando conexão em {HOST}:{PORT}...")

    # Aceita conexões de clientes
    conn, addr = sock.accept()

    print(f"Conectado por {addr[0]}:{addr[1]}")

    # Loop para receber dados do cliente
    while True:
        data = conn.recv(1024)  # Lê dados do cliente
        if not data:            # Se os dados estão vazios, o cliente fechou a conexão
            sock.listen()
            conn, addr = sock.accept()
        #print(f"Dados recebidos: {data.decode()}")  # Imprime os dados recebidos na tela
        if str(data.decode()) == "Evento de Movimentacao":
            resposta = requests.post('http://127.0.0.1:5000/bracelete?tipo=1',data=data)
            print(resposta.json())

        if str(data.decode()) == "Evento de Choro":
            resposta = requests.post('http://127.0.0.1:5000/microfone?tipo=1',data=data)
            print(resposta.json())

    # Fecha a conexão com o cliente e o soquete
    conn.close()
    sock.close()

Inscricao(data)

