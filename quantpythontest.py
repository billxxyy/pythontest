import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn

import numpy as np
import pandas as pd
import tushare as ts

data = ts.get_k_data('600030', start = '2010-01-01', end = '2017-06-30')
data.set_index('date', inplace = True)
data['SMA_20'] = data['close'].rolling(20).mean()
data['SMA_60'] = data['close'].rolling(60).mean()
data[['close', 'SMA_20', 'SMA_60']].plot(figsize = (10, 6))
data['returns'] = np.log(data['close']/data['close'].shift(1))
data['position'] = np.where(data['SMA_20'] > data['SMA_60'], 1, -1)
data['returns'].cumsum().apply(np.exp).plot(figsize=(10, 6))

data1 = ts.get_k_data('600000', start = '2010-01-01', end = '2017-06-30')
data1.set_index('date', inplace = True)
data1['SMA_20'] = data1['close'].rolling(20).mean()
data1['SMA_60'] = data1['close'].rolling(60).mean()
data1[['close', 'SMA_20', 'SMA_60']].plot(figsize = (10, 6))
data1['returns'] = np.log(data1['close']/data1['close'].shift(1))
data1['position'] = np.where(data1['SMA_20'] > data1['SMA_60'], 1, -1)
data1['returns'].cumsum().apply(np.exp).plot(figsize=(10, 6))

plt.show()
