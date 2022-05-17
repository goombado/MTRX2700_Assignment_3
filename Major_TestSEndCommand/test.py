import serial


def serialWrite(com_port):
    serialString = ""      
    serialPort = serial.Serial(port=com_port, baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

    while(1):
        if(serialPort.in_waiting > 0):
            serialPort.write('l 20'.encode('utf-8'))
            serialPort.flush()
            print(serialPort.in_waiting)
    


    
if __name__ == '__main__':
    serialWrite("COM4")