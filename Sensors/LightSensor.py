from Sensor import *

# sudo raspi-config 
# Select Interfacing Options -> i2c-> yes to start the I2C  driver
# sudo reboot

# wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz
# tar zxvf bcm2835-1.60.tar.gz 
# cd bcm2835-1.60/
# sudo ./configure
# sudo make
# sudo make check
# sudo make install
# # For more code, please refer to our official website http://www.airspayce.com/mikem/bcm2835/

# sudo apt-get install wiringpi
# #For Raspberry Pi 4B, an upgrade may be required:
# cd /tmp
# wget https://project-downloads.drogon.net/wiringpi-latest.deb
# sudo dpkg -i wiringpi-latest.deb
# gpio -v
# #Running gpio -v will appear version 2.52. If not, the installation is wrong.

import time
import sys
import os
from waveshare_TSL2591 import TSL2591

class LightSensor(Sensor):

    def __init__(self, name):

        libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
        if os.path.exists(libdir):
            sys.path.append(libdir)

        self.name   = name
        self.sensor = TSL2591.TSL2591()

    def property(self):
        print('Hey, I am a Humidity sensor! My name is ', self.name)

    def LightSensorMeasure(self):
        lux = self.sensor.Lux
        print('Lux: %d'%lux)
        infrared = self.sensor.Read_Infrared
        print('Infrared light: %d'%infrared)
        visible = self.sensor.Read_Visible
        print('Visible light: %d'%visible)
        full_spectrum = self.sensor.Read_FullSpectrum
        print('Full spectrum (IR + visible) light: %d\r\n'%full_spectrum)
    
    def measure(self):
        return self.LightSensorMeasure()

def main():
    w = LightSensor('MyLuxSensor',)
    fp = w.measure()
    print(fp, type(fp))


if __name__ == '__main__':
    main()
