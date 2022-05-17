from Sensor import *
# pip install RPi.bme280
import smbus2
import bme280

class Pressure(Sensor):

    def __init__(self, name, bus=None, address=0x76):
        self.name    = name
        
        port         = 1
        self.address = address
        self.bus     = smbus2.SMBus(port)
        calibration_params = bme280.load_calibration_params(self.bus, self.address)
        self.calibration_params = calibration_params
        
        data = bme280.sample(bus, address, calibration_params)

    def property(self):
        print('Hey, I am a Humidity sensor! My name is ', self.name)

    def PressureMeasure(self):
        data = bme280.sample(self.bus, self.address, self.calibration_params)
        # With this measurement you have also at disposal Temperature and Humidity
        return data.pressure

    def measure(self):
        return self.PressureMeasure()

def main():
    w = Pressure('MyPressureSensor',)
    fp = w.PressureMeasure()
    print(fp, type(fp))


if __name__ == '__main__':
    main()

  # WITH ADAFRUIT
  # import board
  # from adafruit_bme280 import basic as adafruit_bme280
  # # Create sensor object, using the board's default I2C bus.  
  # i2c = board.I2C()  # uses board.SCL and board.SDA
  # bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
  # bme280.temperature/humidity

  # port = 1
  # address = 0x76
  # bus = smbus2.SMBus(port)
  # calibration_params = bme280.load_calibration_params(bus, address)
  # # the sample method will take a single reading and return a
  # compensated_reading object
  # 
  #temperature,pressure,humidity = bme280.readBME280All()
