"""
Initializes for access to the API for an iPython analysis
Usage:
  import init
  a = init.api()
  
"""

import os
import sys


PROJECT_ROOT = "coevolutionmodel"


def getProjectDirectory():
  """
  :return str path:
  """
  path = os.getcwd()
  # Go up to coevolution
  max_iteration = path.count("/")
  found = False
  for n in range(max_iteration):
    last_path = path
    path = os.path.split(path)[0]
    if path.find(PROJECT_ROOT) < 0:
      path = last_path
      found = True
      break
  if not found:
    raise RuntimeError("Could not find project path.")
  return path

def initialize():
  """
  Updates the search path and creates the API object
  :return Api: API object
  """
  python_directory = os.path.join(getProjectDirectory(), PROJECT_ROOT)
  python_directory = os.path.join(python_directory, "Code")
  sys.path.insert(0, python_directory)

initialize()
