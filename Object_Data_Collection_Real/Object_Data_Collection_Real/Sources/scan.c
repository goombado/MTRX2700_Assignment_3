#include <mc9s12dp256.h>
#include <stdio.h>
#include <stdlib.h>

#include "simple_serial.h"
#include "servo.h"
#include "laser.h"


int scanning = 0;
static char buffer[128];
int light_num = 0;
int pb_num = 0;
int pb_presets[8] = {
    128, 192, 224, 240, 248, 252, 254, 255
};


void beginScan (void) {
    
    unsigned long laserSample;
    
    scanning = 1;
    // PORTB = 255;

    sprintf(buffer, "0,");
    SerialOutputString(buffer, &SCI1);
    
    while (scanning) {
        GetLatestLaserSample(&laserSample);

        sprintf(buffer, "%lu,", laserSample);
        SerialOutputString(buffer, &SCI1);
        
        if (light_num == 340) {
            light_num = 0;
            PORTB = pb_presets[pb_num++];
            if (pb_num == 8) {
                pb_num = 0;
            }
        }
        else {
            light_num++;
        }        
            
    }
    
    // Pause_TC6();
    sprintf(buffer, "\r\nEND\r\n");
    SerialOutputString(buffer, &SCI1);
    PORTB = 0;
        
    // exit(1);
}