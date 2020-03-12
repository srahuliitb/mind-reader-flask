import random
import numpy as np

class ShannonExpert:
  inputs = np.zeros(shape=(2, 2, 2), dtype=int) # Follows (z, x, y) format
  last_1 = 0
  last_2 = 0

  def __init__(self):
    self.reset()

  # update the state of the expert given current sequence element. (selected by user)
  def update(self, current):
    if self.inputs[self.last_2][self.last_1][0] == current:
      self.inputs[self.last_2][self.last_1][1] = 1
      self.inputs[self.last_2][self.last_1][0] = current

    else:
      self.inputs[self.last_2][self.last_1][1] = 0
      self.inputs[self.last_2][self.last_1][0] = current
    self.last_1 = current
    self.last_2 = self.last_1
    

  # Produce the prediction for the next bit (0 or 1)
  def predict(self):
    pred = 0

    if self.inputs[self.last_2][self.last_1][1] == 1:
      pred = self.inputs[self.last_2][self.last_1][0]

    else:
      pred = random.randint(0, 1)

    return pred

  # reset expert to original state
  def reset(self):
    for i in range(2):
      for j in range(2):
        for k in range(2):
          self.inputs[k][i][j] = 0

    self.last_1 = random.randint(0, 1)
    self.last_2 = random.randint(0, 1)

