import numpy as np
import math
from resources import *

def function(x, m, k):
  aprime = -1 * (math.sin(x) * (m/k))
  return aprime

@timer
def solver(timestep, tmax, initialv, initialx, m, k):
  tvalues = [0]
  t = np.arange(0,tmax, timestep)
  xvalues = [initialx]
  vvalues = [initialv]
  avalues = [0]
  time = 0
  a_temp = 0
  v_temp = initialv
  x_temp = initialx

  for i in t:

    a_temp = function(x_temp, m, k)
    avalues.append(a_temp)

    v_temp = v_temp + a_temp * timestep
    vvalues.append(v_temp)

    x_temp = x_temp + v_temp * timestep
    xvalues.append(x_temp)

    time += timestep
    tvalues.append(time)

  return xvalues, vvalues, avalues, tvalues

@timer
def rk4(timestep, tmax, initialv, initialx, m, k):
  tvalues = [0]
  t = np.arange(0,tmax, timestep)
  xvalues = [initialx]
  vvalues = [initialv]
  avalues = [0]
  time = 0
  a_temp = 0
  v_temp = initialv
  x_temp = initialx

  for i in t:
    # k1
    # a_temp_k1 = function(x_temp, m, k)
    # v_temp_k1 = a_temp_k1
    # x_temp_k1 = v_temp

    # # k2
    # a_temp_k2 = function(x_temp + 0.5 * timestep * x_temp_k1, m, k)
    # v_temp_k2 = a_temp_k2
    # x_temp_k2 = x_temp + v_temp_k1 * timestep * 0.5

    # # k3
    # a_temp_k3 = function(x_temp + 0.5 * timestep * x_temp_k2, m, k)
    # v_temp_k3 = a_temp_k3
    # x_temp_k3 = x_temp + v_temp_k2 * timestep * 0.5

    # # k4
    # a_temp_k4 = function(x_temp + 0.5 * timestep * x_temp_k3, m, k)
    # v_temp_k4 = a_temp_k4
    # x_temp_k4 = x_temp + v_temp_k3 * timestep

    # # yn + 1
    # v_temp = v_temp + (timestep / 6) * (v_temp_k1 + v_temp_k2 * 2 + v_temp_k3 * 2 + v_temp_k4)
    # x_temp = x_temp + (timestep / 6) * (x_temp_k1 + x_temp_k2 * 2 + x_temp_k3 * 2 + x_temp_k4)

    # time += timestep
    # avalues.append(a_temp_k1)
    # vvalues.append(v_temp)
    # xvalues.append(x_temp)
    # tvalues.append(time)

    # k1
    a1 = function(x_temp, m, k)
    k1x = v_temp
    k1v = a1

    # k2
    x2 = x_temp + 0.5 * timestep * k1x
    v2 = v_temp + 0.5 * timestep * k1v
    a2 = function(x2, m, k)
    k2x = v2
    k2v = a2

    # k3
    x3 = x_temp + 0.5 * timestep * k2x
    v3 = v_temp + 0.5 * timestep * k2v
    a3 = function(x3, m, k)
    k3x = v3
    k3v = a3

    # k4
    x4 = x_temp + timestep * k3x
    v4 = v_temp + timestep * k3v
    a4 = function(x4, m, k)
    k4x = v4
    k4v = a4

    # update
    x_temp += (timestep / 6) * (k1x + 2*k2x + 2*k3x + k4x)
    v_temp += (timestep / 6) * (k1v + 2*k2v + 2*k3v + k4v)

    xvalues.append(x_temp)
    vvalues.append(v_temp)
    avalues.append(function(x_temp, m, k))

  return xvalues, vvalues, avalues, tvalues