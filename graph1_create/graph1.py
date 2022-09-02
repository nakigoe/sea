#Three lines to make our compiler able to draw:
import sys
import matplotlib as mpl
from datetime import datetime, timedelta
from matplotlib.font_manager import FontProperties

import pandas as pd
import matplotlib.pyplot as plt

cmap = mpl.cm.cool #Color map for the temperature graph not working yet 

#custom_date_parser = lambda x: datetime.strptime(x, "%Y/%m/%d %H:%M")
#sea = pd.read_csv('./input/raw_data.csv', parse_dates=['date'], date_parser=custom_date_parser)
sea = pd.read_csv('./input/raw_data.csv')

sea['日時'] = pd.to_datetime(sea['日時'], format = '%Y/%m/%d %H:%M')

sea.plot(kind = 'line', x = '日時', y = '温度', legend=False, figsize=(12, 6.75), yticks=[10,12,14,16,18,20,22,24,26,28,30], colormap=cmap) #figsize: size in inches

#plot formatting:
fp = FontProperties(fname='./fonts/msgothic.ttc', size=19)
fp_label = FontProperties(fname='./fonts/msgothic.ttc', size=15)

plt.title("高知県の水産業の温度[℃]",fontproperties=fp)
plt.ylabel('温度[℃]',fontproperties=fp_label)
plt.xlabel('日時',fontproperties=fp_label)

#saving
tr = datetime.utcnow() + timedelta(milliseconds=0.5) #correct time rounding trick
timestr = tr.strftime("%Y%m%d%H%M%S%f")[:-3]
plt.savefig("./output/graph1_" + timestr + ".svg", format="svg")

#comment the following section out when moving the project to production:
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

