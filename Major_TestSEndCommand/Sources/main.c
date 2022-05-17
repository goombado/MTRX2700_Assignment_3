#include <hidef.h>      /* common defines and macros */
#include "derivative.h"      /* derivative-specific definitions */

#include <string.h>

#include <stdlib.h>

void serialInit(void);
void invalidInput();

interrupt 21 void serialISR();

char buffer[500];
int stringLength = 0;



void main(void) {
  /* put your own code here */
  
  asm("sei");
  
  serialInit();     // Initialising serial port

  EnableInterrupts; // Enabling Interrupts
  
  DDRB = 0xFF;
  


  for(;;) {
    _FEED_COP(); /* feeds the dog */
  } /* loop forever */
  /* please make sure that you never leave main */
}


void serialInit(void) 
{
  // Set baud rate to 9600
  SCI1BDL = 0x9C;
  SCI1BDH = 0;
  
  // No fancy stuff needed
  SCI1CR1 = 0;
  
  // 2C = 0010110, Enable receive interrupt, transmit, receive
  SCI1CR2 = 0x2C;
}


void invalidInput(){
    
    int i;
    char output[16] = " invalidInput\n\r";
    
     for (i = 0; i < 15; i++) 
        {
          while(!(SCI1SR1 & 0x80));
          SCI1DRL = output[i];
        } 
     
       
}

interrupt 21 void serialISR() 
{
  int i;
  char* token;
  char* string;
  // Check if data is received, ie The RDRF flag
  if (SCI1SR1 & 0x20) 
  {
    // Look for a carriage return
    if (SCI1DRL == 0x0D) 
    {   
        
        // Don't do anything unless you are ready to send data. The TDRE flag
        while(!(SCI1SR1 & 0x80));
        buffer[0] = tolower(buffer[0]);   
        if( buffer[0] == 'l'){
           
           string = buffer;
           token = strtok(string, " ");
           token = strtok(NULL, " ");
           token[strlen(token)] = ':';
           token[strlen(token)] = 'L';
           token[strlen(token)] = 'E';
           token[strlen(token)] = 'D';
            
           token[strlen(token)] = '\n';
           token[strlen(token)] = '\r';
            
            if(token == NULL){
               invalidInput();
            } else{                                     
                for(i = 0; i!= strlen(token);i++){
                  while(!(SCI1SR1 & 0x80));
                  SCI1DRL = token[i];
                }
                
                PORTB = atoi(token);
            }
        }
        else{
            invalidInput();
        }
        // Reset buffer
        memset(buffer, '\0' , sizeof(buffer));
        stringLength = 0;

     }
    
    // Store each character of sentence in buffer
    else
    {
      buffer[stringLength] = SCI1DRL;
      stringLength = stringLength + 1;
    }
   
  }
}