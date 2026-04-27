import time
import math
import numpy as np

def timer(func):
  def wrapper(*args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"Took {end_time - start_time} seconds.")
    return result
  return wrapper

def convert_to_positional(theta, length):
  x_pos = length * np.sin(theta)
  y_pos = -length * np.cos(theta)
  return x_pos, y_pos