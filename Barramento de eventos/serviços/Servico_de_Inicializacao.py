import os
import time
import subprocess
import threading
import RPi.GPIO as GPIO

Pino_interrupcao = 17

def callback():
    print("Interrupção acionada!")
    start_time = time.time()
    while GPIO.input(channel) == GPIO.HIGH:
        if time.time() - start_time >= 3:
            encerrar_programas()
            atualizar_arquivo()
            reiniciar_codigo()
            break
        time.sleep(0.1)


# Função para encerrar os subprocessos em execução
def encerrar_programas():
    programas = ['Barramento.py', 'Bracelete.py', 'Camera.py', 'iluminacao.py', 'Microfone.py']
    for programa in programas:
        subprocess.run(["pkill", "-f", programa])


# Função para atualizar o arquivo ChecagemDeinicializacao.log
def atualizar_arquivo():
    with open('ChecagemDeinicializacao.log', 'w') as arquivo:
        arquivo.write('0')


# Função para reiniciar o código a partir do início
def reiniciar_codigo():
    subprocess.run(["python", __file__])
    exit()


# Inicialização da GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(Pino_interrupcao, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Configuração da detecção de interrupção na GPIO
GPIO.add_event_detect(Pino_interrupcao, GPIO.FALLING, callback=callback, bouncetime=200)

def execucaoPadrao():
    # Inicializa 5 programas em threads separadas
    threads = []
    programas = ['Barramento.py', 'Bracelete.py', 'Camera.py', 'iluminacao.py', 'Microfone.py']
    for programa in programas:
        thread = threading.Thread(target=executar_programa, args=(programa,))
        thread.start()
        threads.append(thread)
        time.sleep(1)
    # Aguarda todas as threads terminarem
    for thread in threads:
        thread.join()


# Define uma função para executar cada programa
def executar_programa(programa):
    subprocess.run(["python", programa])
    # os.system(f'.\{programa}')


# Verifica se o arquivo de inicialização existe e contém o valor 1
if os.path.exists('ChecagemDeinicializacao.log'):
    with open('ChecagemDeinicializacao.log', 'r') as arquivo:
        conteudo = arquivo.read().strip()
        # muda para o diretório onde os arquivos Python estão localizados
        # obtém o diretório pai do diretório atual
        diretorio_pai = os.path.dirname(os.getcwd())
        # muda para o diretório pai
        os.chdir(diretorio_pai)
        if conteudo == '1':
            execucaoPadrao()
        else:
            # Inicializa outro programa e captura a saída gerada pelo subprocesso
            processo = subprocess.run(["python", "serviços/Servico_Rede_WIFI.py"], stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)

            # Obtém a saída padrão (stdout) e a saída de erro (stderr) como strings
            saida_padrao = processo.stdout.decode('utf-8').strip()
            saida_erro = processo.stderr.decode('utf-8').strip()

            # Verifica se uma string específica está presente na saída padrão
            if 'Configuracao completa!' in saida_padrao:
                execucaoPadrao()
            else:
                print('Erro:')
                print(saida_erro)

else:
    print('Arquivo de inicialização não encontrado.')

