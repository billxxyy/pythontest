# -*-coding=UTF-8 -*-

import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt

industry = ts.get_industry_classified()
complist = industry[industry['c_name']=='钢铁行业']

fininfo = ts.get_stock_basics()

fininfop = fininfo[fininfo.index.isin(complist['code'])]
fininfop.to_excel(r"/home/shxiao/industry.xlsx", "infop")

plt.plot(fininfop.index, fininfop['pe'])
plt.show()
