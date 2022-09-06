#Three lines to make our compiler able to draw:
import sys
import matplotlib as mpl
from datetime import datetime, timedelta
from matplotlib.font_manager import FontProperties

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import datetime as dt

# explore seaborn vs plt.rcParams:
#import seaborn as sns
#sns.set_theme(style="darkgrid")

cmap = mpl.cm.plasma #Color map for the temperature graph not working yet 
sea = pd.read_csv('./input/raw_data.csv')

#custom_date_parser = lambda x: datetime.strptime(x, "%Y/%m/%d %H:%M")
#sea = pd.read_csv('./input/raw_data.csv', parse_dates=['日時'], date_parser=custom_date_parser)

x = sea['日時'] = pd.to_datetime(sea['日時'], format = '%Y/%m/%d %H:%M')

#display dataframe in conslole, remove when converting for production :
pd.set_option('display.max_columns', None)
sea.head()
print(sea)

#as a variant: yticks=[10,12,14,16,18,20,22,24,26,28,30],

meow = sea.plot(kind = 'line', x = '日時', y = '温度', legend=False, figsize=(12, 6.75), colormap=cmap, marker = 'o', clip_on=False, ms = 8, mec = 'b', mfc = '#4CAF80', lw=2) #figsize: size in inches

# Hide the right and top spines
meow.spines.right.set_visible(False)
meow.spines.top.set_visible(False)

# Only show ticks on the left and bottom spines
meow.yaxis.set_ticks_position('left')
meow.xaxis.set_ticks_position('bottom')

#y ticks step:
start, end = meow.get_ylim()
meow.yaxis.set_ticks(np.arange(int(start), int(end), 1))
meow.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))

#xstart, xend = meow.get_xlim()
#meow.xaxis.set_ticks(np.arange(xstart, xend+1, 1))
#meow.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

#y = range(len(x)) # many thanks to Kyss Tao for setting me straight here
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %H'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gcf().autofmt_xdate()

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

#meow.xaxis.set_major_locator(mdates.HourLocator(interval=10))   #to get a tick every 15 minutes
#meow.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d %H:00'))     #optional formatting 

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

