# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Implementation of the Keras API, the high-level API of TensorFlow.

Detailed documentation and user guides are available at
[keras.io](https://keras.io).

"""

import sys as _sys

from keras import __version__
from keras.api.keras import __internal__
from keras.api.keras import activations
from keras.api.keras import applications
from keras.api.keras import backend
from keras.api.keras import callbacks
from keras.api.keras import constraints
from keras.api.keras import datasets
from keras.api.keras import estimator
from keras.api.keras import experimental
from keras.api.keras import initializers
from keras.api.keras import layers
from keras.api.keras import losses
from keras.api.keras import metrics
from keras.api.keras import mixed_precision
from keras.api.keras import models
from keras.api.keras import optimizers
from keras.api.keras import preprocessing
from keras.api.keras import regularizers
from keras.api.keras import utils
from keras.api.keras import wrappers
from keras.engine.input_layer import Input
from keras.engine.sequential import Sequential
from keras.engine.training import Model
from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras", public_apis=None, deprecation=True,
      has_lite=False)
