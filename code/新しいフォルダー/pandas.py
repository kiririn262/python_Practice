import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn import datasets
boston = datasets. load_boston()
df = DataFrame (boston, data, columns = boston. feature_names)
df.head()