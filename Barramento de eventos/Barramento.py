from flask import Flask, request, Response
import requests
import socket
import json

app = Flask(__name__)

HOST = 'http://127.0.0.1'
PORTA_CAMERA = 8000
PORTA_LUZ = 9000
PORTA_MICROFONE = 7000
PORTA_Bracelete = 3000

IP_Celular = []
PORTA_Celular = []
Usuario = ''
Senha_Usuario = ''
Usuarios = {}


def ler_arquivo_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print("Arquivo não encontrado. Será criado um novo arquivo.")
        return {}


def escrever_arquivo_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        # Escreve o log no arquivo em uma nova linha
        arquivo.write(json.dumps(dados) + '\n')
    # print("Dados salvos com sucesso!")


def adicionar_dicionario(dados, novo_dicionario):
    dados.append(novo_dicionario)
    return dados


nome_arquivo = 'Usuarios/Usuario.json'
dados = ler_arquivo_json(nome_arquivo)


def Autenticar(usuario, senha, IP):
    if IP != '127.0.0.1':
        global Usuario, Senha_Usuario, nome_arquivo
        print(usuario,senha,IP)
        usuario_OK = 0
        senha_OK = 0
        Usr = ler_arquivo_json(nome_arquivo)
        for i in Usr:
            if i['Usuario'] == usuario:
                usuario_OK = 1
        for i in Usr:
            if i['Senha'] == senha:
                senha_OK = 1
        if usuario_OK + senha_OK == 2:
            return 1
        else:
            return -1
    else:
        return 1


# Essa rota serve para inscrever o celular como Observer dos eventos do bebe, para evitar excessivo trafego na rede
@app.route('/', methods=['POST'])
def home():
    global IP_Celular
    global PORTA_Celular
    # Obtém o endereço IP do celular para Avisar quando houver mudanças de estado
    ip = request.remote_addr
    dados = json.loads(request.data.decode())
    print(dados)
    auth = Autenticar(usuario=dados['usuario'], senha=dados['senha'], IP=ip)
    if auth == 1:
        if ip not in IP_Celular:
            IP_Celular.append(ip)
            PORTA_Celular.append(dados['porta'])
            print("Endereço IP do Celular:", IP_Celular)
            print("PORTA do Celular:", PORTA_Celular)
        else:
            print('Celular ja cadastrado')
        return 'usuario autenticado'
    else:
        return 'Credenciais invalidas!'


@app.route('/evento', methods=['POST'])
def ouvir_eventos():
    try:
        global IP_Celular
        global PORTA_Celular
        # Essa rota é para uso exclusivo dos serviços
        if str(request.remote_addr) == '127.0.0.1':
            tipo = int(request.args.get('tipo'))
            if tipo == 1:  # Evento de Movimentacao
                for id, cellIP in enumerate(IP_Celular):
                    print("evento 1")
                    # Cria um objeto de soquete TCP/IP
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    print(f'cell IP: {cellIP}')
                    print(f'cellporta: {PORTA_Celular[id]}')
                    # Conecta o soquete ao servidor remoto em um endereço e porta específicos
                    sock.connect((cellIP, int(PORTA_Celular[id])))
                    # Envia uma mensagem ao servidor
                    message = "Evento de Movimentacao"
                    sock.sendall(message.encode())
                    sock.close()

            if tipo == 2:  # Evento do Microfone
                for id, cellIP in enumerate(IP_Celular):
                    print("evento 2")
                    # Cria um objeto de soquete TCP/IP
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    print(f'cell IP: {cellIP}')
                    print(f'cellporta: {PORTA_Celular[id]}')
                    # Conecta o soquete ao servidor remoto em um endereço e porta específicos
                    sock.connect((cellIP, int(PORTA_Celular[id])))
                    # Envia uma mensagem ao servidor
                    message = "Evento de Choro"
                    sock.sendall(message.encode())
                    sock.close()

            if tipo == 3:  # Evento do Microfone
                for id, cellIP in enumerate(IP_Celular):
                    print("evento 3")
                    # Cria um objeto de soquete TCP/IP
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    print(f'cell IP: {cellIP}')
                    print(f'cellporta: {PORTA_Celular[id]}')
                    # Conecta o soquete ao servidor remoto em um endereço e porta específicos
                    sock.connect((cellIP, int(PORTA_Celular[id])))
                    # Envia uma mensagem ao servidor
                    message = "Evento de Risada"
                    sock.sendall(message.encode())
                    sock.close()

            if tipo == 4:  # Evento do Microfone
                for id, cellIP in enumerate(IP_Celular):
                    print("evento 4")
                    # Cria um objeto de soquete TCP/IP
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    print(f'cell IP: {cellIP}')
                    print(f'cellporta: {PORTA_Celular[id]}')
                    # Conecta o soquete ao servidor remoto em um endereço e porta específicos
                    sock.connect((cellIP, int(PORTA_Celular[id])))
                    # Envia uma mensagem ao servidor
                    message = "Evento de Barulho"
                    sock.sendall(message.encode())
                    sock.close()
            return '200'
        else:
            return 'Voce nao tem autorizacao para acessar esse recurso!'

    except Exception as e:
        # Fecha a conexão com o servidor
        print(e)

        return '500'


@app.route('/camera', methods=['GET'])
# por razões de simplicidade de streaming o método foi alterado para GET,
# porem, o usuário e a senha sao enviados via cabeçalhos, assim podendo continuar usufruindo da criptografia HTTPS TLS
def camera():
    dados = request.headers
    auth = Autenticar(usuario=dados.get('usuario'), senha=dados.get('senha'), IP=request.remote_addr)
    if auth == 1:
        tipo = int(request.args.get('tipo'))
        if tipo == 1:
            print("Imagem requisitada")
            resposta = requests.get(f'{HOST}:{PORTA_CAMERA}/imagem', stream=False)
            return Response(resposta,
                            content_type=resposta.headers['Content-Type'])
        else:
            print("Video requisitado")
            resposta = requests.get(f'{HOST}:{PORTA_CAMERA}/video', stream=True)
            return Response(resposta.iter_content(chunk_size=1024),
                            content_type=resposta.headers['Content-Type'],
                            status=resposta.status_code)
    else:
        return 'Credenciais invalidas!'


@app.route('/microfone', methods=['POST'])
def audio():
    dados = json.loads(request.data.decode())
    auth = Autenticar(usuario=dados['usuario'], senha=dados['senha'], IP=request.remote_addr)
    if auth == 1:
        tipo = int(request.args.get('tipo'))
        if tipo == 1:
            resposta = requests.get(f'{HOST}:{PORTA_MICROFONE}/microfone')
            return resposta.json()
        if tipo == 2:
            resposta = requests.get(f'{HOST}:{PORTA_MICROFONE}/microfoneLog')
            return resposta.json()
    else:
        return 'Credenciais invalidas!'


@app.route('/iluminacao', methods=['POST'])
def iluminacao():
    dados = json.loads(request.data.decode())
    auth = Autenticar(usuario=dados['usuario'], senha=dados['senha'], IP=request.remote_addr)
    if auth == 1:
        tipo = int(request.args.get('tipo'))
        if tipo == 1:
            resposta = requests.get(f'{HOST}:{PORTA_LUZ}/Ligar')
            return resposta.json()
        if tipo == 2:
            resposta = requests.get(f'{HOST}:{PORTA_LUZ}/Desligar')
            return resposta.json()
        if tipo == 3:
            resposta = requests.get(f'{HOST}:{PORTA_LUZ}/Status')
            return resposta.json()
    else:
        return 'Credenciais invalidas!'


@app.route('/bracelete', methods=['POST'])
def bracelete():
    dados = json.loads(request.data.decode())
    auth = Autenticar(usuario=dados['usuario'], senha=dados['senha'], IP=request.remote_addr)
    if auth == 1:
        tipo = int(request.args.get('tipo'))
        if tipo == 1:
            resposta = requests.get(f'{HOST}:{PORTA_Bracelete}/Status')
            return resposta.json()
        else:
            resposta = requests.get(f'{HOST}:{PORTA_Bracelete}/Logs')
            return resposta.json()
    else:
        return 'Credenciais invalidas!'


if __name__ == '__main__':
    # app.run()
    wind = 1
    linux = 0
    if wind == 1:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print("Endereço IP da rede:", ip)
    if linux == 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        print("Endereço IP da rede:", ip)

    app.run(host='0.0.0.0', port=5000)  # para a interface de loopback (localhost)
    app.run(host=ip, port=5000)  # para a interface de rede externa
