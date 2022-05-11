import numpy as np
from tifffile import *


class TemperatureMeasure:

    def __init__(self):
        pass

    def measure(self):
        return 10

    def measure_avg_3(self):
        avg = (30 + self.measure() + self.measure()) / 3
        return avg


class MatrixMeasure:

    def __init__(self):
        pass

    def gen_matrix(self):
        data = np.random.randint(30, 255, (300, 300, 300), 'uint8')
        return data


if __name__ == "__main__":
    # bella = TemperatureMeasure()
    # a = bella.measure()
    # print(a, bella.measure())

    mat = MatrixMeasure()
    matrix = mat.gen_matrix()
    imwrite('temp.tif', matrix, photometric='rgb')
    imwrite('temp2.tif', matrix, photometric='minisblack')