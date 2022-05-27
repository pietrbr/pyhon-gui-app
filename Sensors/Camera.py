# TO BE FINISHED

# sudo pip3 install matplotlib scipy numpy
# sudo apt-get install -y python-smbus
# sudo apt-get install -y i2c-tools
# sudo reboot
# The address for I2C of Camera should be 0x33

# sudo pip3 install RPI.GPIO adafruit-blinka
# sudo pip3 install adafruit-circuitpython-mlx90640

import board, busio
import numpy as np
import adafruit_mlx90640
from scipy import ndimage

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000)
# begin MLX90640 with I2C comm
mlx = adafruit_mlx90640.MLX90640(i2c)
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ  # set refresh rate
# mlx90640 shape
mlx_shape = (24, 32)

# # IF u want to interpolate
# mlx_interp_val = 10 # interpolate # on each dimension
# mlx_interp_shape = (mlx_shape[0]*mlx_interp_val,
#                     mlx_shape[1]*mlx_interp_val) # new shape

frame = np.zeros(mlx_shape[0] * mlx_shape[1])  # 768 pts
while True:
    try:
        mlx.getFrame(frame)  # read MLX temperatures into frame var
        break
    except ValueError:
        continue  # if error, just read again

# print out the average temperature from the MLX90640
print('Average MLX90640 Temperature: {0:2.1f}C'.\
      format(np.mean(frame)))
