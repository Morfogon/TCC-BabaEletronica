import machine
from imu import MPU6050
import math
import time
limiar_balanco_bebe = 30

# Configura o barramento I2C para comunicação com o acelerômetro
i2c = machine.I2C(1, freq=400000)
imu = MPU6050(i2c)

# Configura os pinos UART0 para comunicação Bluetooth
uart = machine.UART(0, baudrate=38400)

# Define a função para enviar dados via Bluetooth
def send_data(data):

    # Envia os dados via Bluetooth
    uart.write(data)

# Define a função de interrupção para o pino 2
while True:
    x_accel = int(imu.gyro.x)
    y_accel = int(imu.gyro.y)
    z_accel = int(imu.gyro.z)

    # Verifica se houve uma forte movimentação (aceleração superior a 1 m/s^2)
    if int(math.sqrt((x_accel**2)+(y_accel**2)+(z_accel**2))) > limiar_balanco_bebe:
        print("Bebe se movimentou!")
        temp=round(imu.temperature,2)
        # Monta a string de dados a ser enviada via Bluetooth
        data=f"Bebe se movimentou!, temp = {temp}\r\n"
        # Envia os dados via Bluetooth
        send_data(data)
        time.sleep(1)
    time.sleep(1)



