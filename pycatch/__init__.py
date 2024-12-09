from pycatch import pycatch
from typeguard import typechecked
import numpy as np

@typechecked
def compute(x: np.ndarray, n:int) -> float:
    return pycatch.compute(x, n)

@typechecked
def zscore(x: np.ndarray) -> np.ndarray:
    return pycatch.zscore(x)