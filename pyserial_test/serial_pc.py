"""import serial

#シリアル通信
print("Open port")
ser = serial.Serial()
ser.port = "COM3"      #デバイスマネージャーでarduinoのポート確認
ser.baudrate = 9600    #arduinoと合わせる
ser.setDTR(False)      #DTRを常にLOWにしReset阻止
ser.open()             #COMポートを開く
ser.write(b"1")        #送りたい内容をバイト列で送信
ser.close()            #COMポートを閉じる
print("Close port")"""

import serial

 
#シリアル通信(PC⇔Arduino)

ser = serial.Serial()
 
ser.port = "COM3"     #デバイスマネージャでArduinoのポート確認
 
ser.baudrate = 9600 #Arduinoと合わせる
 
ser.setDTR(False)     #DTRを常にLOWにしReset阻止
 
ser.open()            #COMポートを開く
 
ser.write(b'2')       #送りたい内容をバイト列で送信
 
ser.close()           #COMポートを閉じる