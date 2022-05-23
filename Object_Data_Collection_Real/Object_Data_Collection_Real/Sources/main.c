#include <hidef.h>      /* common defines and macros */
#include <assert.h>
#include "derivative.h"      /* derivative-specific definitions */

// need this for string functions
#include <stdio.h>
#include <stdlib.h>

#include "pll.h"
#include "simple_serial.h"

#include "l3g4200d.h"

#include "servo.h"
#include "laser.h"

#include "gyro.h"



void printErrorCode(IIC_ERRORS error_code) {
  char buffer[128];  
  switch (error_code) {
    case NO_ERROR: 
      sprintf(buffer, "IIC: No error\r\n");
      break;
    
    case NO_RESPONSE: 
      sprintf(buffer, "IIC: No response\r\n");
      break;
    
    case NAK_RESPONSE:
      sprintf(buffer, "IIC: No acknowledge\r\n");
      break;
    
    case IIB_CLEAR_TIMEOUT:
      sprintf(buffer, "IIC: Timeout waiting for reply\r\n");
      break;
    
    case IIB_SET_TIMEOUT: 
      sprintf(buffer, "IIC: Timeout not set\r\n");
      break;
    
    case RECEIVE_TIMEOUT:
      sprintf(buffer, "IIC: Received timeout\r\n");
      break;
    
    case IIC_DATA_SIZE_TOO_SMALL:
      sprintf(buffer, "IIC: Data size incorrect\r\n");
      break;

    default:
      sprintf(buffer, "IIC: Unknown error\r\n");
      break;
  }
    
  SerialOutputString(buffer, &SCI1);
}



void main(void) {

    AccelRaw read_accel;
//    AccelScaled scaled_accel;

    GyroRaw read_gyro;
    
    static char buffer[128];
    unsigned long laserSample;
    int prev_toggle = 0;
    
    IIC_ERRORS error_code = NO_ERROR;
    
    PLL_Init();
    
    PWMinitialise();
    setServoPose(50 + MIN_ITER, 0);
    
    // exit(1);
    
    SerialInitialise(BAUD_9600, &SCI1);
    
    error_code = iicSensorInit();
    if (error_code != NO_ERROR) {
        sprintf(buffer, "Error setting up IIC\r\n");
        SerialOutputString(buffer, &SCI1);
    }
    
    sprintf(buffer, "laser,gyro_x,gyro_y,gyro_z\r\n\r\n");
    SerialOutputString(buffer, &SCI1);
    
    laserInit();
    
    Init_TC6();
    
    sprintf(buffer, "\r\nSCAN 1 - Left to Right\r\n");
    SerialOutputString(buffer, &SCI1);

    EnableInterrupts;
    
    _DISABLE_COP();
    
    for(;;) {
    
        error_code = getRawDataGyro(&read_gyro);   
    
        if (error_code != NO_ERROR) {
          printErrorCode(error_code);   
           
          error_code = iicSensorInit();
          printErrorCode(error_code);   
        }
        
        error_code = getRawDataAccel(&read_accel);
        if (error_code != NO_ERROR) {
          printErrorCode(error_code);   
        
          error_code = iicSensorInit();
          printErrorCode(error_code); 
        }


        GetLatestLaserSample(&laserSample);
        
        sprintf(buffer, "%lu,%d,%d,%d\r\n", laserSample, read_gyro.x, read_gyro.y, read_gyro.z);
        SerialOutputString(buffer, &SCI1);
        
        /*
        if (prev_toggle != toggle) {
            prev_toggle = toggle;
            sprintf(buffer, "NEXT SCAN\r\n");
            SerialOutputString(buffer, &SCI1);
        }
        */
        
    } 
  
}