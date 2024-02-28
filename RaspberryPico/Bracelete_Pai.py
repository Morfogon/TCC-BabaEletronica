import machine
import math
import time

# Define o número do pino que deseja configurar
pin_number = 2

# Configura o pino como saída
pin = machine.Pin(pin_number, machine.Pin.OUT)

# Configura os pinos UART0 para comunicação Bluetooth
uart = machine.UART(0, baudrate=9600)

# Define a função de interrupção para o pino 2
while True:
    a=uart.read()
    if a!=None:
        print(a)
        pin.value(1)
        time.sleep(2)
        pin.value(0)
    time.sleep(3)

