from pycatch22 import pycatch22
from typeguard import typechecked
import numpy as np

@typechecked
def compute(x: np.ndarray, n:int) -> float:
    return pycatch22.compute(x, n)

@typechecked
def zscore(x: np.ndarray) -> np.ndarray:
    return pycatch22.zscore(x)