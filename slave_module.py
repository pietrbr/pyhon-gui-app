class TemperatureMeasure:
    def __init__(self):
        pass
    
    def measure(self):
        return 10
    
    def measure_avg_3(self):
        avg = (30 + self.measure() + self.measure()) / 3
        return avg

if __name__ == "__main__":
    bella = TemperatureMeasure()
    a = bella.measure()
    print(a, bella.measure())