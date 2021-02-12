from flask import Flask, render_template, request
import numpy as np
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
        message = 'ArduinoのLEDの明るさを設定できます')

@app.route('/', methods=['POST'])
def post():
    bri = request.form.get('range')

    #2/12
    #成功した
    ser.open()
    ser.write(bytes(bri, "UTF-8"))
    ser.close()

    #2/11
    """
    ser.open()
    ser.write(str.encode(bri))
    ser.close()
    """    

    #~2/11
    #bri_charcode = ord(bri[0])
    #print(bri_charcode)
    #print(type(bri))
    #s_bri = str(bri)
    
    #s8_bri = s_bri.astype('uint8')
    #print(s8_bri)
    """
    s_bri = np.uint8(bri)
    #s8_bri = s_bri.astype('uint8')
    print(type(s_bri))
    ser.open()
    ser.write(s_bri)
    ser.close()

    """

    
        
    return render_template('index.html', \
        title = 'Success!', \
        message = 'ArduinoのLEDを{}にしました！'.format(bri))
        
        
    
        
        


if __name__ == '__main__':
    app.run()