#import PySimpleGUI as sg 
import serial
import sys
import glob
import time

#ser = None  #Global tanımlanmalı
#ser = serial.Serial(
#    port="COM1", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
#)

def serial_ports():
    if sys.platform.startswith('win'):  # windows kullanılıyorsa
        ports = ['COM%s' % (i + 1) for i in range(5)] # Hız için 256'dan 32'e düşürüldü.
      #yukarıdaki satırdaki komut i nin for döngüsüyle artarak array şeklinde yazılmasını sağlıyor. 
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

# aşağıdakiler açılabilecek portların listesini veriyor. 
    result = []
    print(ports)
    
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
        print("port")
        print(port)
        print("result  ")
        print(result)
    return result

def serial_baglan():
    com_deger = 'COM1'
    baud_deger = '9600'
    print("Baud Deger", '9600')
    global ser
    ser = serial.Serial(com_deger, baud_deger, timeout=0, parity=serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE , bytesize = serial.EIGHTBITS, rtscts=0)
    print("Bağlandi...", sep='\n')
#def oku():
serial_baglan()
while True:
    ser.write('2'.encode('Ascii'))
    data=ser.readline(1)
    print(data, sep='\n')
    print("port")
    print("result  ")
    time.sleep(0.1)
    if data == b'A':    
        ser.close
        print('Loop exited')
        break
    
