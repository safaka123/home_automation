import serial

print(serial.__version__)
ser = serial.Serial('COM1', 9600)
ser.write('OKU'.encode('Ascii'))
ser.close()
