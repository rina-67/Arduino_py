from flask import Flask, render_template, request
import serial

app = Flask(__name__)


ser = serial.Serial()
ser.port = 'COM3'
ser.baudrate = 9600
ser.setDTR(False)


@app.route('/', methods=['GET'])
def get():
    return render_template('index.html', \
        title = 'Arduino_LED(not set)', \
        message = 'ArduinoのLEDの色を設定できます')

@app.route('/', methods=['POST'])
def post():
    name = request.form.get('radio')
    if name == 'off':
        
        ser.open()
        ser.write(b'0')
        ser.close()
        
        return render_template('index.html', \
            title = 'Sucsess!', \
            message = 'ArduinoのLEDを{}にしました！'.format(name))
    else:
        
        ser.open()
        ser.write(b'1')
        ser.close()
        
        return render_template('index.html', \
            title = 'Sucsess!', \
            message = 'ArduinoのLEDを{}にしました！'.format(name))


if __name__ == '__main__':
    app.run()