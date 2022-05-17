import serial

serialPort = serial.Serial(port="COM4", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

while(1):
    
    if(serialPort.in_waiting > 0):
        serialPort.write(str.encode('l 20'))
        serialPort.flush()
        print(serialPort.in_waiting)
