import numpy as np
import pandas as pd

path = 'datasets/iris.csv'

df = pd.read_csv(filepath_or_buffer = path, sep = ',')
print(df)