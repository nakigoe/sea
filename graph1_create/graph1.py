import matplotlib as mpl
from datetime import datetime, timedelta
from matplotlib.font_manager import FontProperties

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

def make_graph1():

    mpl.rc('font', family='MS Gothic')

    reveresd_sea = pd.read_csv('./input/raw_data.csv') #the original data comes in the reversed order, inverse:
    sea = reveresd_sea.iloc[::-1]

    cmap = mpl.cm.plasma #Default 'plasma' color map is too wide, narrow to the temperature of 4-30 (sea temperature)

    graph = sea.plot(kind = 'line', x = '日時', y = '温度', legend=False, figsize=(12, 6.75), colormap=cmap, marker = 'o', clip_on=False, ms = 8, mec = 'b', mfc = '#4CAF80', lw=2) #figsize: size in inches

    # Hide the right and top spines
    graph.spines.right.set_visible(False)
    graph.spines.top.set_visible(False)

    # Only show ticks on the left and bottom spines
    graph.yaxis.set_ticks_position('left')
    graph.xaxis.set_ticks_position('bottom')

    #y ticks step:
    start, end = graph.get_ylim()
    #compensate y label for the upper limit
    if end-int(end) < 0.25 and abs(start-end)>2:
        end+=1
    else: 
        end+=2

    graph.yaxis.set_ticks(np.arange(int(start), int(end), 1))
    graph.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))

    #--------------------------x-axis formatting--------------------------
    x = pd.to_datetime(sea['日時'], format = '%Y/%m/%d %H:%M')
    total_hours = round((x.iloc[-1]-x.iloc[0]).total_seconds() / 3600)

    graph.xaxis_date()
    xstart = 0
    xend=total_hours
    graph.xaxis.set_ticks(np.arange(xstart, xend+1, 1))
    graph.set_xticklabels(sea['日時'].str[5:].str.replace('/','月').str.replace(' ','日 '))
    plt.gcf().autofmt_xdate()

    # Disjoin bottom / left spines by moving them outwards
    for s in ['bottom', 'left']: graph.spines[s].set_position(('outward', 12))

    #plot formatting:
    fp = FontProperties(fname='./fonts/msgothic.ttc', size=19)
    fp_label = FontProperties(fname='./fonts/msgothic.ttc', size=15)

    plt.title("高知県の水産業の温度[℃]",fontproperties=fp,pad=13)
    plt.ylabel('温\n度\n℃',fontproperties=fp_label, rotation=0, ha='right', labelpad=13)

    year = x.iloc[-1].strftime("%Y")
    plt.xlabel('日時'+ year +'年',fontproperties=fp_label, labelpad=10)

    plt.xticks(rotation = 45, ha = 'right')
    plt.tight_layout()

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
        'ytick.minor.pad': 15
        })

    plt.grid(axis = 'y', color = 'grey', linewidth = 0.334)

    #saving
    tr = datetime.utcnow() + timedelta(milliseconds=0.5) #correct time rounding trick
    timestr = tr.strftime("%Y%m%d%H%M%S%f")[:-3]
    plt.savefig("./output/graph1_" + timestr + ".svg", format="svg", dpi=360)

    #plt.show()

make_graph1()

