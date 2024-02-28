import machine
import time
import uos

# Configurar a porta serial (UART) USB
uart_port = machine.UART(0, baudrate=9600)  # Usando a porta UART USB

# Configurar o pino de controle do relé
relay_pin = machine.Pin(2, machine.Pin.OUT)  # Usando o pino GP2

def main():
    while True:
        if uart_port.any():
            received_data = uart_port.read(1)  # Lê um byte da porta serial
            print(received_data)
            if received_data == b'1':  # Valor recebido para ativar o relé
                relay_pin.on()
                print("Módulo de relé ativado.")
            elif received_data == b'0':  # Valor recebido para desativar o relé
                relay_pin.off()
                print("Módulo de relé desativado.")

        time.sleep(0.1)  # Pequena pausa para evitar leitura contínua

if __name__ == "__main__":
    main()
