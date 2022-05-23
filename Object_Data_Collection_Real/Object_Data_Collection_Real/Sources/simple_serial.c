#include <mc9s12dp256.h>        /* derivative information */
#include <stdio.h>

#include "simple_serial.h"
#include "scan.h"


// instantiate the serial port parameters
//   note: the complexity is hidden in the c file
SerialPort SCI1 = {&SCI1BDH, &SCI1BDL, &SCI1CR1, &SCI1CR2, &SCI1DRL, &SCI1SR1};
SerialPort SCI0 = {&SCI0BDH, &SCI0BDL, &SCI0CR1, &SCI0CR2, &SCI0DRL, &SCI0SR1};


int stringLength = 0;
static char buffer[128];


// InitialiseSerial - Initialise the serial port SCI1
// Input: baudRate is tha baud rate in bits/sec
void SerialInitialise(int baudRate, SerialPort *serial_port) {
  
  // Baud rate calculation from datasheet
  switch(baudRate){
	case BAUD_9600:
      *(serial_port->BaudHigh)=0;
      *(serial_port->BaudLow)=156;
	  break;
	case BAUD_19200:
      *(serial_port->BaudHigh)=0;
      *(serial_port->BaudLow)=78;
	  break;
	case BAUD_38400:
      *(serial_port->BaudHigh)=0;
      *(serial_port->BaudLow)=39;
	  break;
	case BAUD_57600:
      *(serial_port->BaudHigh)=0;
      *(serial_port->BaudLow)=26;
	  break;
	case BAUD_115200:
      *(serial_port->BaudHigh)=0;
      *(serial_port->BaudLow)=13;
	  break;
  }
  
  *(serial_port->ControlRegister2) = SCI1CR2_RE_MASK | SCI1CR2_TE_MASK | SCI1CR2_RIE_MASK;
  *(serial_port->ControlRegister1) = 0x00;
}
    
        
void SerialOutputChar(char data, SerialPort *serial_port) {  
  while((*(serial_port->StatusRegister) & SCI1SR1_TDRE_MASK) == 0){
  }
  
  *(serial_port->DataRegister) = data;
}



void SerialOutputString(char *pt, SerialPort *serial_port) {
  while(*pt) {
    SerialOutputChar(*pt, serial_port);
    pt++;
  }            
}



#pragma CODE_SEG __NEAR_SEG NON_BANKED
__interrupt void serialISR() {

  if (scanning == 1) {
    return;
  }
  
  // Check if data is received, ie The RDRF flag
  if (*(SCI1.StatusRegister) & 0x20) 
  {
    PORTB = 255;
    // Look for a carriage return
    if (SCI1DRL == 0x0D) 
    {   
        
        // Don't do anything unless you are ready to send data. The TDRE flag
        while(!(SCI1SR1 & 0x80));
        
        beginScan();
        
        // Reset buffer
        memset(buffer, '\0' , sizeof(buffer));
        stringLength = 0;

     }
    
    // Store each character of sentence in buffer
    else
    {
      buffer[stringLength] = *(SCI1.DataRegister);
      stringLength = stringLength + 1;
    }
   
  }
  PORTB = 255;
}



