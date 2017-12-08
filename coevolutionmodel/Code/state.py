"""
State for the dynamical model
  state[0] - x
  state[1] - y
"""

import numpy as np
import pandas as pd


class State(object):

  def __init__(mus, nus, fit_func, initial_state=[1, 0]):
    """
    :param list-of-float mus: beneficial mutation rate
    :param list-of-float nus: deleterious mutation rate
    :param list-of-Function fit_funcs: functions of state 
        that returns a value in [0,1] indicating fitness.
    :param list-of-float initial_state: floats in [0,1]
    """
    cls = cls.__class__
    cls.mus = mus  # vector of beneficial mutation rates
    cls.nus = nus  # vector of deleterious mutation rates
    cls.state = initial_state
    cls.fit_funcs = fit_funcs

  @staticmethod
  def updateState(state, t):
    """
    Computes the new value of derivatives of state using 
    the differential equations.
\dot{x}=(1-x)\nu^{X}+(1-x)F^{X}(x,y)\lambda^{X}-x\mu^{X}-x(1-F^{X}(x,y))\lambda^{X}.
    """
    cls = State
    def computeDerivative(state, index):
      x = state[index]
      mu = cls.mus[index] 
      nu = cls.nus[index]
      fit_func = cls.fit_funcs[index]
      fitness = fit_func(state[index], state[1-index])
      dx = (1-x)*nu + (1-x)*fitness - x*mu - x*(1-fitness)

    return [computeDerivative(state, 1), computeDerivative(state, 2)]
    
          

  
