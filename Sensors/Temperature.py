# ! pip3 install adafruit-circuitpython-dht
import board
import adafruit_dht


class DHT22():

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

        try:
            # Print the values to the serial port
            temperature_c = self.sensor.temperature
            # temperature_f = temperature_c * (9 / 5) + 32
            humidity = self.sensor.humidity
            # Check if you want to return also humidity from here
            return temperature_c, humidity

        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            return None, None
        except Exception as error:
            # self.sensor.exit()
            # raise error
            return None, None

    def measure(self):
<<<<<<< HEAD
        value = None
        while value == None:
            value = self.TemperatureMeasure()
        return value
=======
        temperature, humidity = None, None
        while temperature == None or humidity == None:
            temperature, humidity = self.TemperatureMeasure()
        return temperature, humidity
>>>>>>> 4a088287b276c4df40f2df04d418e38ed0976fa1


def main():
    w = DHT22('Sensore di Temperatura')
    fp = w.measure()
    print(fp, type(fp))


if __name__ == '__main__':
    main()
