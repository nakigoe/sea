#Three lines to make our compiler able to draw:
import sys
import matplotlib as mpl
from datetime import datetime, timedelta
from matplotlib.font_manager import FontProperties

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# explore seaborn vs plt.rcParams:
#import seaborn as sns
#sns.set_theme(style="darkgrid")

cmap = mpl.cm.cool #Color map for the temperature graph not working yet 
sea = pd.read_csv('./input/raw_data.csv')

#custom_date_parser = lambda x: datetime.strptime(x, "%Y/%m/%d %H:%M")
#sea = pd.read_csv('./input/raw_data.csv', parse_dates=['日時'], date_parser=custom_date_parser)

sea['日時'] = pd.to_datetime(sea['日時'], format = '%Y/%m/%d %H:%M')

#as a variant: yticks=[10,12,14,16,18,20,22,24,26,28,30],

meow = sea.plot(kind = 'line', x = '日時', y = '温度', legend=False, figsize=(12, 6.75),  colormap=cmap, marker = 'o', ms = 8, mec = 'b', mfc = '#4CAF80', lw=2) #figsize: size in inches

# Disjoin bottom / left spines by moving them outwards
for s in ['bottom', 'left']: meow.spines[s].set_position(('outward', 12))

#plot formatting:
fp = FontProperties(fname='./fonts/msgothic.ttc', size=19)
fp_label = FontProperties(fname='./fonts/msgothic.ttc', size=15)

plt.title("高知県の水産業の温度[℃]",fontproperties=fp)
plt.ylabel('温\n度\n℃',fontproperties=fp_label, rotation=0, ha='right', labelpad=13)
plt.xlabel('日時',fontproperties=fp_label)
plt.xticks(rotation = 45, ha = 'right')
plt.tight_layout()

#the following section has no effect for some reason, seaborn theme interfering?
plt.rcParams.update({
    'font.size': 12,
    'axes.edgecolor': 'gray',
    'xtick.color':    'gray',
    'ytick.color':    'gray',
    'axes.labelcolor':'gray',
    'axes.spines.right':False,
    'axes.spines.top':  False,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.size': 6,
    'xtick.minor.size': 4,
    'ytick.major.size': 6,
    'ytick.minor.size': 4,
    'xtick.major.pad': 15,
    'xtick.minor.pad': 15,
    'ytick.major.pad': 15,
    'ytick.minor.pad': 15,
    })
plt.grid(axis = 'y', color = 'grey', linewidth = 0.334)
#saving
tr = datetime.utcnow() + timedelta(milliseconds=0.5) #correct time rounding trick
timestr = tr.strftime("%Y%m%d%H%M%S%f")[:-3]
plt.savefig("./output/graph1_" + timestr + ".svg", format="svg", dpi=360)

#comment the following section out when moving the project to production:
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

#in the plan: find max, min temperature values to adopt vertical limits

