import numpy as np
from csv import DictWriter


class TemperatureMeasure:

    def __init__(self):
        pass

    def measure(self):
        return 10

    def measure_avg_3(self):
        avg = (30 + self.measure() + self.measure()) / 3
        return avg


if __name__ == "__main__":
    # bella = TemperatureMeasure()
    # a = bella.measure()
    # print(a, bella.measure())

    headersCSV = ['ID', 'NAME', 'SUBJECT']
    dict = {'ID': '04', 'NAME': 'John', 'SUBJECT': 'Mathematics'}

    with open('CSVFILE.csv', 'a', newline='') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
        dictwriter_object.writerow(dict)
        f_object.close()
