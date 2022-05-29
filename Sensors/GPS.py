# GPS Module

# sudo nano /boot/config.txt

# add to the file the following lines

# dtparam=spi=on
# dtoverlay=pi3-disable-bt
# core_freq=250
# enable_uart=1
# force_turbo=1

# # Create a backup copym for safety reason
# sudo cp /boot/cmdline.txt /boot/cmdline_backup.txt

# sudo nano /boot/cmdline.txt
# dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles
# sudo reboot

# # Check which port is related with serial0
# # sudo systemctl stop serial-getty@ttyAMA0.service
# # sudo systemctl disable serial-getty@ttyAMA0.service

# sudo systemctl stop serial-getty@ttyS0.service
# sudo systemctl disable serial-getty@ttyS0.service

# # pip install pynmea2

import serial
import time
import string
import pynmea2


class GPS():

    def __init__(self, name='Sensore GPS', port="/dev/ttyAMA0"):
        self.name = name
        self.port = port
        self.ser = serial.Serial(port, baudrate=9600, timeout=0.5)

    def property(self):
        print('Hey, I am a GPS sensor! My name is ', self.name)

    def GPSMeasure(self):
        flag = True
        i = 0
        max_iteration = 100
        while flag and i < max_iteration:
            i += 1
            dataout = pynmea2.NMEAStreamReader()
            newdata = self.ser.readline()

            if newdata[0:6] == "$GPRMC":

                flag = False
                newmsg = pynmea2.parse(newdata)
                lat = newmsg.latitude
                lng = newmsg.longitude
                # gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
                # print(gps)
                return lat,lng

        print('Failure')
        return None, None

    def measure(self):
        return self.GPSMeasure()


def main():
    w = GPS(name='MyGPSSensor', port="/dev/ttyAMA0")
    fp = w.measure()
    print(fp, type(fp))


if __name__ == '__main__':
    main()
