import serial


def serialWrite(com_port):
    serialString = ""      
    serialPort = serial.Serial(port=com_port, baudrate=9600, bytesize=8, timeout=2, write_timeout = None ,parity = serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

    byte = serialPort.write(b'A\n\r')
    serialPort.flush()

    print("Byte written: ", byte )
    
    serialPort.close()

    """
    while(1):
        if(serialPort.in_waiting > 0):
            serialPort.write('l 20'.encode('utf-8'))
            serialPort.flush()
            print(serialPort.in_waiting)
    
    """
    


    
if __name__ == '__main__':
    serialWrite("COM8")