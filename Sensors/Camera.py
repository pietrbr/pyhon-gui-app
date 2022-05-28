# pip install PyMLX90614

# from smbus2 import SMBus
import smbus
import time
from mlx90614 import MLX90614

class MLX90614_GY906():

    def __init__(self, name='Camera Ad Infrarosso Per la Temperatura Superficiale'):
        self.name = name
        # Your InfraRed sensor will be an instance of DHT22
        bus = smbus.SMBus(1)
        self.sensor = MLX90614(bus, address=0x5A)
    
    def TemperatureMeasure(self):
        return self.sensor.get_amb_temp()

    def measure(self):
        tempSuperficiale = 0
        n_meas = 10
        for i in range(n_meas):
            tempSuperficiale = tempSuperficiale + self.sensor.get_obj_temp()/n_meas
            time.sleep(0.2)
        return tempSuperficiale

def main():
    w = MLX90614_GY906('Sensore di Temperatura Superficiale')
    fp = w.measure()
    print(fp, type(fp))

if __name__ == '__main__':
    main()
