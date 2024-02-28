import time
from datetime import datetime
from flask import Flask, request, send_file, render_template, url_for, make_response, jsonify, Response
import threading
import serial
import json
import requests

# Porta serial a qual o HC-05 está conectado (verifique o gerenciador de dispositivos)
port = "COM3"
# Velocidade de comunicação
baudrate = 38400
# Timeout para leitura serial
timeout = 1

# Inicializa a conexão serial
ser = serial.Serial(port, baudrate, timeout=timeout)

log = {}

app = Flask(__name__)

global_data = ''
global_erro_status = ''
global_hora_deteccao = ''
global_dia_deteccao = ''


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


# Ler o arquivo CSV e transformar em JSON
nome_arquivo = 'Logs/Logs_Movimento.json'
# Lê os dados do arquivo JSON
dados = ler_arquivo_json(nome_arquivo)


def receber_dados():
    global global_data
    global global_erro_status
    global global_hora_deteccao
    global global_dia_deteccao
    global dados
    global nome_arquivo
    global log

    while True:
        try:
            # Lê uma linha da porta serial
            line = ser.readline()
            # Verifica se a linha não está vazia
            global_data = line.decode()
            global_hora_deteccao = ''
            global_dia_deteccao = ''
            if line:
                hora_atual = datetime.now().hour
                minuto_atual = datetime.now().minute
                data_atual = datetime.now()
                dia_atual = data_atual.day
                mes_atual = data_atual.month
                ano_atual = data_atual.year
                global_hora_deteccao = f'{hora_atual}:{minuto_atual}'
                global_dia_deteccao = f'{dia_atual}/{mes_atual}/{ano_atual}'
                # Imprimir o resultado da predição com a hora e o minuto atual
                log.update({'Estado': 'Movimento', 'hora': hora_atual, 'minuto': minuto_atual, 'dia': dia_atual,
                            'mes': mes_atual,
                            'ano': ano_atual,
                            'TEMPERATURA': global_data.split(',')[1].replace('temp = ', '').strip()})

                dados = adicionar_dicionario(dados, log)
                escrever_arquivo_json(nome_arquivo, dados)

                # Imprime a linha recebida na tela
                print("Recebido:", global_data)
                requests.post('http://127.0.0.1:5000/evento?tipo=1')

                time.sleep(3)
            time.sleep(1)

        except Exception as e:
            ser.close()
            global_erro_status = e


# Inicia a thread para receber dados
recebe_thread = threading.Thread(target=receber_dados)
recebe_thread.start()

try:
    @app.route('/Status')
    def Status():
        global global_data
        global global_erro_status
        global global_hora_deteccao
        global global_dia_deteccao

        if global_erro_status == '':
            print('Dados recebidos: ' + global_data)
            return make_response(
                jsonify({'Estado': global_data.split(',')[0].strip(), 'HORA': global_hora_deteccao,
                         'DIA': global_dia_deteccao,
                         'TEMPERATURA': global_data.split(',')[1].replace('temp = ', '').strip()}), 200)
        else:
            print('ERRO: ' + global_erro_status)
            return make_response(jsonify({'Estado': 'ERRO', 'ERRO': global_erro_status}), 500)


    @app.route('/Logs')
    def Logs():
        response = {'Logs': ler_arquivo_json(nome_arquivo)}
        return make_response(jsonify(response), 200)

except Exception:
    recebe_thread.join()

if __name__ == '__main__':
    app.run(port=3000)
