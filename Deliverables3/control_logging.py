#this is the code that eds provided.

import serial
import datetime
import time
import busio #serial protocol supporter
from board import SCL, SDA
import argparse

#import the PCA9685 module.
from adafruit_pca9685 import PCA9685

def logging(filename):
    #Create the I2C bus interface
    i2c_bus = busio.I2C(SCL, SDA)

    #Create a simple PC9685 class instance.
    pca = PCA9685(i2c_bus)

    #Set the PWM frequency to 60hz.
    pca.frequency = 90

    f = open(filename, 'w')

    with serial.Serial('/dev/ttyUSB0', 9600, timeout=10) as ser: #open serial port
        start = input('Do you want to start logging?')[0]
        if start in 'yY':
            ser.write(bytes('YES\n', 'utf-8'))
            while True:
                ser_in = ser.readline().decode('utf-8')
                print(ser_in)
                f.write("{} {}".format(datetime.datetime.now(), ser_in))
                print("{} {}".format(datetime.datetime.now(), ser_in), end=' ')
                steer = int(ser_in.split(' ')[2].split('/')[0])
                throttle = int(ser_in.split(' ')[5].split('/')[0])

    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('log_file_name', metavar='F', type=str, nargs=1, help="log file's name")
    args = parser.parse_args()
    logging(args.log_file_name)
