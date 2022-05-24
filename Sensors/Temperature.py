from Sensor import *
# ! pip3 install adafruit-circuitpython-dht
import board
import adafruit_dht


class Temperature(Sensor):

    def __init__(self, name='DHT22'):
        self.name = name
        # Your temperature sensor will be an instance of DHT22
        self.sensor = adafruit_dht.DHT22(board.D4, use_pulseio=False)

    def property(self):
        print('Hey, I am a Temperature sensor! My name is ', self.name)

    def TemperatureMeasure(self):
        # Set the import and dhtDevice object outside
        # Put the import in the main

        # Initial the dht device, with data pin connected to:
        # dhtDevice = adafruit_dht.DHT22(board.D18)

        # you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
        # This may be necessary on a Linux single board computer like the Raspberry Pi,
        # but it will not work in CircuitPython.

        # MAKE A CLASS SENSORS to handle every sensor
        dhtDevice = self.sensor

        try:
            # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            # temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            print("Temp: {:.1f} C    Humidity: {}% ".format(
                temperature_c, humidity))

            # Check if you want to return also humidity from here
            return temperature_c

        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
        except Exception as error:
            dhtDevice.exit()
            raise error

    def measure(self):
        return self.TemperatureMeasure()

    def dht22_measure_temperature(self):
        dhtDevice = self.sensor
        return dhtDevice.temperature

    def dht22_measure_pressure(self):
        dhtDevice = self.sensor
        return dhtDevice.pressure


def main():
    w = Temperature('MyTemperatureSensor', )
    fp = w.measure()
    print(fp, type(fp))


if __name__ == '__main__':
    main()