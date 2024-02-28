import time
import socket
import serial
import subprocess
import json

port = "COM7"  # porta de ENTRADA (COM7) ≥ O dispositivo que inicia a conexão
# Velocidade de comunicação
baudrate = 9600
# Timeout para leitura serial
timeout = 1
REDE = ''
SENHA = ''
Usuario = ''
Senha_Usuario = ''
Usuarios = {}
# Inicializa a conexão serial
ser = serial.Serial(port, baudrate, timeout=timeout)


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


def Criar_Conta():
    global Usuario, Senha_Usuario, Usuarios, dados
    ser.write('CONEXAO BEM SUCEDIDA\r\n'.encode())
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    ser.write('O endereço IP da baba:\r\n'.encode())
    ser.write(ip.encode())
    ser.write('\r\nCriacao de conta da baba\r\n'.encode())
    ser.write('Digite o usuario\r\n'.encode())
    while True:
        Usuario = ser.readline().decode()
        if Usuario:
            break
    ser.write('Digite a Senha\r\n'.encode())
    while True:
        Senha_Usuario = ser.readline().decode()
        if Senha_Usuario:
            break
    Usuarios.update({'Usuario': Usuario.replace('\r\n', ''), 'Senha': Senha_Usuario.replace('\r\n', '')})
    dados = adicionar_dicionario(dados, Usuarios)
    escrever_arquivo_json(nome_arquivo, dados)
    print('Usuarios:', Usuario, ' Senha:', Senha_Usuario)
    ser.write('Cadastrar outro usuario? SIM = 1 Nao = 0\r\n'.encode())
    while True:
        escolha = ser.readline().decode()
        if escolha:
            break
    if int(escolha) == 1:
        Criar_Conta()
    ser.write('Configuracao completa!\r\n'.encode())


def Conexao(erro=0, msg_erro=''):
    if erro == 0:
        ser.write(b"Digite o nome da sua rede WIFI:\r\n")
    else:
        ser.write(b"Ocorreu um erro ao se conectar a rede WIFI:\r\n")
        ser.write(msg_erro.encode())
        time.sleep(2)
        Conexao(erro=0)
    # Loop infinito para ouvir continuamente na porta serial
    while True:
        # Lê uma linha da porta serial
        line = ser.readline()
        # Verifica se a linha não está vazia
        if line:
            # Imprime a linha recebida na tela
            REDE = line.decode()
            print("RECEBIDO:", REDE)
            break
    msg = f'Digite sua senha rede WIFI {REDE}:'
    ser.write(msg.encode())
    while True:

        # Lê uma linha da porta serial
        line = ser.readline()
        # Verifica se a linha não está vazia
        if line:
            # Imprime a linha recebida na tela
            SENHA = line.decode()
            print("RECEBIDO:", SENHA)
            break


try:
    ser.write(b"Bem vindo!\r\n")

    Conexao()

    # Cria o conteúdo do arquivo de configuração wpa_supplicant
    wpa_supplicant_conf = f"""
    country=BR
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    
    network={{
        ssid="{REDE}"
        psk="{SENHA}"
    }}
    """
    # Escreve o conteúdo do arquivo de configuração em um arquivo temporário
    with open("/tmp/wpa_supplicant.conf", "w") as f:
        f.write(wpa_supplicant_conf)

    # Copia o arquivo temporário para o local correto
    subprocess.run(["sudo", "cp", "/tmp/wpa_supplicant.conf", "/etc/wpa_supplicant/wpa_supplicant.conf"])

    # Ativa e desativa a interface Wi-Fi para se conectar à rede
    ifconfig_result = subprocess.run(["sudo", "ifdown", "wlan0"], capture_output=True)
    if ifconfig_result.returncode == 0:
        ifconfig_result = subprocess.run(["sudo", "ifup", "wlan0"], capture_output=True)
        if ifconfig_result.returncode == 0:
            status = 0
        else:
            status = -1
    else:
        status = -1

    # Exibe o status da interface Wi-Fi ou o valor de status
    if status == 0:
        subprocess.run(["ifconfig", "wlan0"])
        Criar_Conta()
    else:
        msg = f"Erro ao se conectar à rede {REDE}. Status: {status}"
        print(msg)
        Conexao(erro=1, msg_erro=msg)

    # Fecha a conexão serial
    ser.close()
except Exception as e:
    print(e)
    ser.write(f'Ocorreu um erro inesperado: {e}\r\n'.encode())
    ser.close()
