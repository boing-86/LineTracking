import serial
import datetime
import time
import logging
import busio #serial protocol supporter
from board import SCL, SDA

#import the PCA9685 module.
from adafruit_pca9685 import PCA9685

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
#formatter = logging.Formatter('%(message)s')
file_handler = logging.FileHandler('05311827.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#with serial.Serial('/dev/ttyACM0', 9600, timeout=5) as ser: #open serial port
arduino = serial.Serial(
port = '/dev/ttyACM0',
baudrate = 9600,
bytesize = serial.EIGHTBITS,
parity = serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE,
timeout = 5,
xonxoff = False,
rtscts = False,
dsrdtr = False,
writeTimeout = 2
)

#Create the I2C bus interface
i2c_bus = busio.I2C(SCL, SDA)

#Create a simple PC9685 class instance.
pca = PCA9685(i2c_bus)

pca.frequency = 74

valuet = 7777 #7760 or 7940
valuec = 7800
stop = 7600
center = 7700
left = 9700
right = 5700
        
print("Ready")
pca.channels[0].duty_cycle = center
pca.channels[1].duty_cycle = valuet
time.sleep(3)

while True:                                                     
    try :
        arduino.write("Command from Jetson".encode())
        data = arduino.readline()

        if data :
            data = data.decode()
            print("\nload : ") # print received data from arduino to console
            print(data)
                
            if ('0 0 1 1 0 0' in data): #전진 
                steer = center
                throttle = valuet

            elif ('0 1 1 1 0 0' in data) : #좌회전1
                steer = 8100
                throttle = valuet
                
            elif ('0 1 1 0 0 0' in data) : #좌회전1.5
                steer = 8500
                throttle = valuet
                
            elif ('1 1 1 0 0 0' in data) : #좌회전2
                steer = 8900
                throttle = valuec

            elif ('1 1 0 0 0 0' in data) : #좌회전2.5
                steer = 9300
                throttle = valuec
            
            elif ('1 0 0 0 0 0' in data) : #좌회전3
                steer = 10200
                throttle = valuec
                
            elif ('0 0 1 1 1 0' in data) : #우회전1
                steer = 7300
                throttle = valuet
                        
            elif ('0 0 0 1 1 0' in data) : #우회전1.5
                steer = 6900
                throttle = valuet

            elif ('0 0 0 1 1 1' in data) : #우회전2
                steer = 6500
                throttle = valuec
                
            elif ('0 0 0 0 1 1' in data) : #우회전2.5
                steer = 6100
                throttle = valuec

            elif ('0 0 0 0 0 1' in data) : #우회전3
                steer = 5200
                throttle = valuec
                        
            elif ('0 0 0 0 0 0' in data):#input X
                steer = 5200
                throttle = valuec

            elif ('0 1 1 1 0 1' in data):#stop
                pca.channels[0].duty_cycle = center
                pca.channels[1].duty_cycle = stop
                break
                
            else :
                steer = center
                throttle = valuec
                
            pca.channels[0].duty_cycle = steer
            pca.channels[1].duty_cycle = throttle

            logger.info(steer)
            logger.info(throttle)
            logger.info(data)

    except Exception as e:
        print(e)
        continue
