#esp32
import machine
import time
import uos
import urequests
import network

# Configuração da rede Wi-Fi
SSID = "SuaRedeWiFi"
PASSWORD = "SuaSenhaWiFi"

# Endereço do servidor
SERVER_IP = "192.168.0.214"
ILUMINACAO_ENDPOINT = "/iluminacao?tipo=4"

# Configurar o pino de controle do relé
relay_pin = machine.Pin(2, machine.Pin.OUT)  # Usando o pino GP2

# Função para conectar à rede Wi-Fi e enviar a requisição de iluminação
def conectar_wifi():
    station = network.WLAN(network.STA_IF)
    station.active(True)
    if not station.isconnected():
        print("Conectando à rede WiFi...")
        station.connect(SSID, PASSWORD)
        while not station.isconnected():
            pass
        print("Conectado à rede WiFi.")
        print("Endereço IP:", station.ifconfig()[0])

        # Envia a requisição para /iluminacao?tipo=4 ao conectar à rede
        url_iluminacao = f"http://{SERVER_IP}{ILUMINACAO_ENDPOINT}"
        dados = '{"porta": 2001, "usuario": "124", "senha": "124ert"}'
        try:
            response = urequests.post(url_iluminacao, data=dados)
            if response.status_code == 200:
                print("Requisição de iluminação enviada com sucesso.")
            else:
                print("Erro ao enviar a requisição de iluminação.")
        except Exception as e:
            print("Erro ao enviar a requisição de iluminação:", e)

# Função para acionar o relé
def acionar_rele(estado):
    if estado == 'Ligar':
        relay_pin.on()
        print("Módulo de relé ativado.")
    elif estado == 'Desligar':
        relay_pin.off()
        print("Módulo de relé desativado.")

# Função principal
def main():
    conectar_wifi()

    while True:
        try:
            # Verifica os endpoints para controle remoto
            url_ligar = f"http://{SERVER_IP}{RELAY_ENDPOINT_LIGAR}"
            url_desligar = f"http://{SERVER_IP}{RELAY_ENDPOINT_DESLIGAR}"

            response_ligar = urequests.get(url_ligar)
            if response_ligar.status_code == 200:
                print("Comando de ligar recebido via HTTP.")
                acionar_rele('Ligar')

            response_desligar = urequests.get(url_desligar)
            if response_desligar.status_code == 200:
                print("Comando de desligar recebido via HTTP.")
                acionar_rele('Desligar')

        except Exception as e:
            print("Erro:", e)

        time.sleep(0.1)  # Pequena pausa para evitar leitura contínua

if __name__ == "__main__":
    main()
