#ifndef SERVO_H
#define SERVO_H


#define ZERO_ELEVATION_DUTY 4200
#define ZERO_AZIMUTH_DUTY 4400
#define MAX_ELEVATION_DUTY 5050
#define MAX_AZIMUTH_DUTY 5250
#define MIN_ELEVATION_DUTY 3450
#define MIN_AZIMUTH_DUTY 3650

#define BASE_ITERATIONS 1600
#define MIN_ITER -850
#define MAX_ITER 750
#define INCREMENT_NUM 1
#define MAX_SCANS 4
#define SCAN_EVERY_X 1


extern int toggle;


void PWMinitialise(void);

// sets servo in elevation and azimuth
// note: this requires verification and calibration 
void setServoPose(int azimuth, int elevation);


// interrupt used for cycling through the servo positions
__interrupt void TC6_ISR(void);

void Init_TC6 (void);


#endif