import matplotlib.pyplot as plt
import seaborn
import matplotlib as mpl
import numpy as np
import pandas as pd
import tushare as ts

data = ts.get_k_data('600030', start = '2010-01-01', end = '2017-06-30')
data.set_index('date', inplace = True)
