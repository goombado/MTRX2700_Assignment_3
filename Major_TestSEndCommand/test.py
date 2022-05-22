import serial
import time

def serialWrite(com_port):
    serialString = ""      
    serialPort = serial.Serial(port=com_port, baudrate=9600, bytesize=serial.EIGHTBITS, timeout=2, write_timeout = 0, xonxoff=True, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    time.sleep(3)   # Only needed for Arduino,For AVR/PIC/MSP430 & other Micros not needed
                # opening the serial port from Python will reset the Arduino.
                # Both Arduino and Python code are sharing Com11 here.
                # 3 second delay allows the Arduino to settle down.


    # BytesWritten = serialPort.write(b'A\n\r')      #transmit 'A' (8bit) to micro/Arduino
    # serialPort.flush()

    # print('BytesWritten = ', BytesWritten)
    
    """ BytesWritten = serialPort.write('k'.encode('utf_8'))      #transmit 'A' (8bit) to micro/Arduino
    serialPort.flush()
    print('BytesWritten = ', BytesWritten)
    time.sleep(3) """

    BytesWritten = serialPort.write(b'l')      #transmit 'A' (8bit) to micro/Arduino
    serialPort.flush()
    print('BytesWritten = ', BytesWritten)
    BytesWritten = serialPort.write(b'\r')      #transmit 'A' (8bit) to micro/Arduino
    serialPort.flush()
    print('BytesWritten = ', BytesWritten)
    BytesWritten = serialPort.write(b'\n')      #transmit 'A' (8bit) to micro/Arduino
    serialPort.flush()
    print('BytesWritten = ', BytesWritten)

    serialPort.close()    

    """
    while(1):
        if(serialPort.out_waiting > 0):
            serialPort.write('l 20\n\r'.encode('utf-8'))
            serialPort.flush()
            print("yes")
        else:
            time.sleep(0.05)
    """


    
if __name__ == '__main__':
    serialWrite("COM4")
    