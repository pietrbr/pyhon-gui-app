class Sensor():
  def __init__(self, name):
      self.name = name

  def property(self):
      print('Hey, I am a general sensor!')

  def measure(self):
      print('The job of a sensor is to measure')