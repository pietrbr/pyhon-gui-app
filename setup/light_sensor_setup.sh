cd Documents
echo "Select Interfacing Options -> i2c-> yes to start the I2C  driver"
sudo raspi-config 
sudo reboot

wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz
tar zxvf bcm2835-1.60.tar.gz 
cd bcm2835-1.60/
sudo ./configure
sudo make
sudo make check
sudo make install
# For more code, please refer to our official website http://www.airspayce.com/mikem/bcm2835/

cd Documents
sudo apt-get install wiringpi
#For Raspberry Pi 4B, an upgrade may be required:
cd /tmp
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
gpio -v
#Running gpio -v will appear version 2.52. If not, the installation is wrong.