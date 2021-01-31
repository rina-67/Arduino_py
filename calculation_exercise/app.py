from flask import Flask, render_template, request
import serial
import numpy as np

app = Flask(__name__)


ser = serial.Serial()
ser.port = 'COM3'
ser.baudrate = 9600
ser.setDTR(False)


@app.route('/', methods=['GET'])
def get():
    num = np.random.randint(1,10,2)
    global c_ans
    c_ans = num[0] + num[1]
    return render_template('index.html', \
        title = '足し算してみよう！', \
        message = '正解するとArduinoのLEDが光ります', \
        exercise = '{} + {} ='.format(num[0],num[1]))

@app.route('/', methods=['POST'])
def post():
    y_ans = request.form.get('text')
    if c_ans == int(y_ans):
        
        ser.open()
        ser.write(b'1')
        ser.close()
        
        return render_template('index.html', \
            title = '正解！😄', \
            message = '次の計算も頑張ってね')
    else:
        
        ser.open()
        ser.write(b'0')
        ser.close()
        
        return render_template('index.html', \
            title = '不正解!😞', \
            message = '正解は{}だよ'.format(c_ans))


if __name__ == '__main__':
    app.run()