#include <mc9s12dp256.h>
#include <stdio.h>
#include <stdlib.h>

#include "simple_serial.h"
#include "servo.h"
#include "laser.h"


int scanning = 0;
static char buffer[128];


void beginScan (void) {
    
    unsigned long laserSample;
    
    scanning = 1;
    PORTB = 254;
    
    // laserInit();
    
    // Init_TC6();

    sprintf(buffer, "0,");
    SerialOutputString(buffer, &SCI1);
    
    while (scanning) {
        GetLatestLaserSample(&laserSample);

        sprintf(buffer, "%lu,", laserSample);
        SerialOutputString(buffer, &SCI1);
    }
    
    // Pause_TC6();
    PORTB = 0;
        
    // exit(1);
}