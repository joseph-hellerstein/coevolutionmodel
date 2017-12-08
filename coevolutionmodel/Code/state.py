"""
State for the dynamical model
  state[0] - x
  state[1] - y
"""

import numpy as np
import pandas as pd

DEFAULT_MU = 4*10e-9
DEFAULT_NU = 2*10e-3
DEFAULT_MU = 1*10e-1
DEFAULT_NU = 2*10e-1
DELTA = 0.5
FITNESS = 0.48
DEFAULT_FUNC = lambda x,y: FITNESS*(1 - x*(1-y)*DELTA)

class State(object):

  @classmethod
  def init(cls,
      mus = [DEFAULT_MU, DEFAULT_MU], 
      nus = [DEFAULT_NU, DEFAULT_NU], 
      fit_funcs = [DEFAULT_FUNC, DEFAULT_FUNC], 
      initial_state=[1, 0]):
    """
    :param list-of-float mus: beneficial mutation rate
    :param list-of-float nus: deleterious mutation rate
    :param list-of-Function fit_funcs: functions of state 
        that returns a value in [0,1] indicating fitness.
    :param list-of-float initial_state: floats in [0,1]
    """
    cls.mus = mus  # vector of beneficial mutation rates
    cls.nus = nus  # vector of deleterious mutation rates
    cls.state = initial_state
    cls.fit_funcs = fit_funcs

  @staticmethod
  def update(state, t):
    """
    Computes the new value of derivatives of state using 
    the differential equations.
    """
    cls = State
    def computeDerivative(state, index):
      x = state[index]
      mu = cls.mus[index] 
      nu = cls.nus[index]
      fit_func = cls.fit_funcs[index]
      fitness = fit_func(state[index], state[1-index])
      dx = (1-x)*nu + (1-x)*fitness - x*mu - x*(1-fitness)
      return dx

    result = [computeDerivative(state, 0), 
        computeDerivative(state, 1)]
    return result
