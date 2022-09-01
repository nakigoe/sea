#Three lines to make our compiler able to draw:
import sys
import matplotlib
import time
from datetime import datetime, timedelta
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams

import pandas as pd
import matplotlib.pyplot as plt

#matplotlib.use('Agg')

sea = pd.read_csv('./input/raw_data.csv')
sea.plot()

#plot formatting:
fp = FontProperties(fname='./fonts/KaishoMCBK1Pro-DeBold.otf', size=20)
fp_label = FontProperties(fname='./fonts/KaishoMCBK1Pro-DeBold.otf', size=14)
rcParams['font.family'] = fp.get_name()

plt.title("高知県の水産業の温度[℃]",fontproperties=fp)
plt.ylabel('温度[℃]',fontproperties=fp_label)

#saving
tr = datetime.utcnow() + timedelta(milliseconds=0.5) #correct time rounding trick
timestr = tr.strftime("%Y%m%d%H%M%S%f")[:-3]
plt.savefig("./output/graph1_" + timestr + ".svg", format="svg")

#comment the following section out when moving the project to production:
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

