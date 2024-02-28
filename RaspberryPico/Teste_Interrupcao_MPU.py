import machine
from imu import MPU6050

# endereço do MPU6050
MPU_ADDR = 0x68

# registradores do MPU6050
REG_PWR_MGMT_1 = 0x6B
REG_CONFIG = 0x1A
REG_INT_ENABLE = 0x38
REG_ACCEL_CONFIG = 0x1C

# valores dos registradores
VAL_PWR_MGMT_1 = 0x00  # habilita o MPU6050
VAL_CONFIG = 0x01  # desabilita o filtro
VAL_INT_ENABLE = 0x01  # habilita a interrupção
VAL_ACCEL_CONFIG = 0x01  # define a escala de aceleração como +/- 2g

interrupt_pin = machine.Pin(2, machine.Pin.IN)
sda_pin = machine.Pin(6, machine.Pin.IN)
scl_pin = machine.Pin(7, machine.Pin.IN)


limiar_balanco_bebe = 2

# Configura o barramento I2C para comunicação com o acelerômetro
i2c = machine.I2C(1, freq=400000)
devices = i2c.scan()
imu = MPU6050(i2c)


# Verifica se o MPU6050 está conectado
if MPU_ADDR not in devices:
    raise ValueError("MPU6050 não encontrado.")

# Habilita o MPU6050
i2c.writeto_mem(MPU_ADDR, REG_PWR_MGMT_1, bytearray([VAL_PWR_MGMT_1]))

# Configuração do filtro
i2c.writeto_mem(MPU_ADDR, REG_CONFIG, bytearray([VAL_CONFIG]))

# Configuração da interrupção
i2c.writeto_mem(MPU_ADDR, REG_INT_ENABLE, bytearray([VAL_INT_ENABLE]))

# Configuração da escala de aceleração
i2c.writeto_mem(MPU_ADDR, REG_ACCEL_CONFIG, bytearray([VAL_ACCEL_CONFIG]))



# Configura os pinos UART0 para comunicação Bluetooth
uart = machine.UART(0, baudrate=38400)

# Configura o pino 2 como entrada
pino2 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

# Define a função para enviar dados via Bluetooth
def send_data(data):
    # Ativa o módulo Bluetooth
    #uart.write(b'AT+MODE=1\r\n')

    # Envia os dados via Bluetooth
    uart.write(data)
    machine.lightsleep(1000)

# Define a função de interrupção para o pino 2
def on_interrupt(pin):
    x_accel = round(imu.accel.x)
    y_accel = round(imu.accel.y)
    z_accel = round(imu.accel.z)

    # Verifica se houve uma forte movimentação (aceleração superior a 1 m/s^2)
    print(f'valores {x_accel} {y_accel} {z_accel} \n ', end='\r')
    if abs(x_accel) > limiar_balanco_bebe or abs(y_accel) > limiar_balanco_bebe or abs(z_accel) > limiar_balanco_bebe :
        print("aquii")
        # Monta a string de dados a ser enviada via Bluetooth
        data="Bebe se movimentou!\r\n"
        # Envia os dados via Bluetooth
        send_data(data)
    else:
        machine.lightsleep(1000)

# Configura a interrupção no pino 2
pino2.irq(trigger=machine.Pin.IRQ_FALLING, handler=on_interrupt)

# Entra em um estado de baixo consumo de energia, esperando pela interrupção no pino 2
machine.lightsleep()

