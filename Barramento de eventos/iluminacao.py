from flask import Flask, request, send_file, render_template, url_for, make_response, jsonify, Response
import serial

# Configurar a porta serial (UART) USB
uart_port = serial.Serial('COM7', baudrate=9600, timeout=1)
app = Flask(__name__)
Estado = 0

try:
    @app.route('/Ligar')
    def Ligar():
        global Estado
        Estado = 1
        uart_port.write(b'0')  # Envia '1' via UART
        return make_response(jsonify({'Estado': 'Ligado'}), 200)


    @app.route('/Desligar')
    def Desligar():
        global Estado
        Estado = 0
        uart_port.write(b'1')  # Envia '0' via UART
        return make_response(jsonify({'Estado': 'Desligado'}), 200)


    @app.route('/Status')
    def Status():
        global Estado
        if Estado == 1:
            return make_response(jsonify({'Estado': 'Ligado'}), 200)
        else:
            return make_response(jsonify({'Estado': 'Desligado'}), 200)
except Exception as e:
    print(e)

if __name__ == '__main__':
    app.run(port=9000)
