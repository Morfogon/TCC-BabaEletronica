import subprocess
import time
import psutil
import gc
from multiprocessing import Process, Queue
from threading import Thread
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def iniciar_servico(servico, queue):
    processo = subprocess.Popen(['python', servico], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Thread para capturar saídas (logs) do processo
    def capturar_saida():
        for linha in iter(processo.stdout.readline, ''):
            queue.put(f"{servico} (stdout): {linha.strip()}")
        for linha in iter(processo.stderr.readline, ''):
            queue.put(f"{servico} (stderr): {linha.strip()}")

    t = Thread(target=capturar_saida)
    t.start()

    # Espera o término do processo
    processo.wait()

    # Sinaliza o término da thread de captura de saídas
    t.join()

def monitorar_recursos(processos):
    try:
        while True:
            time.sleep(5)  # Intervalo entre verificações de uso de recursos

            # Limpa o terminal antes de cada novo print
            limpar_terminal()

            # Lógica para monitorar e exibir uso de recursos
            uso_total_cpu = 0
            uso_total_memoria = 0

            for servico, processo in processos.items():
                try:
                    info = psutil.Process(processo.pid)
                    uso_cpu = info.cpu_percent()
                    uso_memoria = info.memory_info().rss

                    print(f"Uso de recursos para {servico}: {uso_cpu:.2f}% CPU, {uso_memoria / (1024 * 1024):.2f} MB de memória")

                    uso_total_cpu += uso_cpu
                    uso_total_memoria += uso_memoria
                except psutil.NoSuchProcess:
                    # Ignora processos que não existem mais
                    print(f"Ignorando {servico} porque o processo não foi encontrado.")

            print(f"Uso Total de Recursos: {uso_total_cpu:.2f}% CPU, {uso_total_memoria / (1024 * 1024):.2f} MB de memória")

            # Lógica para limpar a memória
            gc.collect()

            # Lógica para verificar o estado dos processos e recriar em caso de falha
            for servico, processo in processos.items():
                if not processo.is_alive():
                    print(f"Recriando {servico} porque falhou.")
                    processos[servico] = Process(target=iniciar_servico, args=(servico, Queue()))
                    processos[servico].start()

    except KeyboardInterrupt:
        # Encerra todos os processos quando o script é interrompido
        for processo in processos.values():
            processo.terminate()

if __name__ == '__main__':
    # Lista de nomes dos serviços
    servicos = ['Barramento.py', 'Microfone.py', 'Camera.py']

    # Dicionário para mapear processos aos seus respectivos serviços
    processos = {servico: Process(target=iniciar_servico, args=(servico, Queue())) for servico in servicos}

    for processo in processos.values():
        processo.start()

    # Chama a função para monitorar os recursos
    monitorar_recursos(processos)
