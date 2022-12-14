#code by Maxim Angel, email: teachermaxim@gmail.com
#You see the latest version at https://github.com/nakigoe/sea/blob/main/graph1_create/graph1.py

import matplotlib as mpl
from datetime import datetime, timedelta
from matplotlib.font_manager import FontProperties

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

def make_graph1():
    #total graph size with margins in inches:
    total_width=12
    total_height=6.75

    #margins in 0.01 of the plot width and height, that is, the dimensions of the whole graph is a number between 0 ~ 1
    graph_left_margin=0.025 #left margin is 2.5% of the image size
    graph_right_margin=0.025 #right margin is 2.5% of the image size
    graph_top_margin=0.03 #top margin is 3% of the image size
    graph_bottom_margin=0.03 #bottom margin is 3% the image size

    #graph_inner_width_in_onehundredth is a number between 0 ~ 1, graph width in percentages after the margins are subtracted!!!
    graph_inner_width_in_onehundredth=1-graph_right_margin-graph_left_margin 

    #graph_inner_height_in_onehundredth is a number between 0 ~ 1, graph height in percentages after the margins are subtracted!!!
    graph_inner_height_in_onehundredth=1-graph_top_margin-graph_bottom_margin 

    graph_width = total_width * graph_inner_width_in_onehundredth #graph width in inches without margins
    graph_height = total_height * graph_inner_height_in_onehundredth #graph width in inches without margins

    marker_size=min(graph_width, graph_height)
    if marker_size<5: marker_size=5 #minimum marker size for small screens
    if marker_size>8: marker_size=8 #maximum marker size for larger screens

    #outer border, black line, set automatically. Change to manual if necessary.
    border_width=max(graph_width, graph_height)
    if border_width<2: border_width=2
    if border_width>16: border_width=16

    mpl.rc('font', family='MS Gothic', weight='bold')

    reveresed_sea = pd.read_csv('./input/raw_data.csv') #the original data comes in the reversed order, inverse:
    sea = reveresed_sea.iloc[::-1]

    temperature = sea['??????']
    timeline = sea['??????']

    #------------------------------- black border around the graph -----------------------------------
    fig = plt.figure(figsize=(total_width, total_height), linewidth=border_width, edgecolor="#000") 
    ax = fig.add_subplot()
    ax.plot(timeline, temperature, '-', marker = 'o', clip_on=False, ms = marker_size, mec = 'b', mfc = '#4CAF80', lw=2, rasterized=False)  

    # Show the right and top spines
    ax.spines.right.set_visible(True)
    ax.spines.top.set_visible(True)

    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    #-------------------------- x-axis formatting --------------------------
    python_hours_array = pd.to_datetime(sea['??????'], format = '%Y/%m/%d %H:%M')
    total_hours = round((python_hours_array.iloc[-1] - python_hours_array.iloc[0]).total_seconds() / 3600)

    ax.xaxis_date()
    xstart = 0
    xend=total_hours
    ax.xaxis.set_ticks(np.arange(xstart, xend+1, 1))
    ax.set_xticklabels(sea['??????'].str[5:].str.replace(' ','\n')) #an alternative is to rotate 45 deg and to use: .str.replace('/','???').str.replace(' ','???\n'))
    #plt.xticks(rotation = 45, ha = 'right')
    #plt.gcf().autofmt_xdate() #autorotate the labels if necessary, the angle is set automatically

    #----------------------- labels frequency section -------------------
    hours_distance=1
    if graph_width < 18: hours_distance=2
    if graph_width < 9: hours_distance=3
    if graph_width < 6: hours_distance=4
    if graph_width < 5: hours_distance=6
    if graph_width < 4: hours_distance=8
    if graph_width < 3: hours_distance=12
    ax.xaxis.set(major_locator=mpl.ticker.MultipleLocator(hours_distance))

    celsius_distance=1
    if graph_height < 7: celsius_distance=2
    if graph_height < 6: celsius_distance=3
    if graph_height < 5: celsius_distance=4
    if graph_height < 4: celsius_distance=5
    if graph_height < 3: celsius_distance=6
    if graph_height < 2: celsius_distance=7
    if graph_height < 1: celsius_distance=8
    ax.yaxis.set(major_locator=mpl.ticker.MultipleLocator(celsius_distance))

    #---------------- y ticks start and end position -----------------
    start, end = ax.get_ylim()
    #compensate y label for the upper limit
    if end-int(end) < 0.25 and abs(start-end)>2:
        end+=celsius_distance
    else: 
        end+=2*celsius_distance

    #or you can set the lowest possible sea temperature manually, like it is done now in 2022 by my client's request. You can safely remove the following line to set the lowest temperature automatically:
    if start > 10: start=10 #that is, the client asked to set the lower graph limit to 10??C if the temperature is higher than 10??C

    ax.yaxis.set_ticks(np.arange(int(start), int(end), celsius_distance))
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))

    # Disjoin bottom / left spines by moving them outwards
    #for s in ['bottom', 'left']: ax.spines[s].set_position(('outward', 12))

    #font formatting:
    fp_xticklabel=FontProperties(family=['Sans-Serif','Arial', 'Verdana','Helvetica'], weight='semibold', size=12)
    fp_yticklabel=FontProperties(family=['Sans-Serif', 'Arial', 'Verdana','Helvetica'], weight='semibold', size=12)
    #Just in case the Japanese font 'MS Gothic' is not installed on the system, grab it from the SEA root folder:
    fp = FontProperties(fname='../fonts/msgothic.ttc', size=19)
    fp_label = FontProperties(fname='../fonts/msgothic.ttc', size=16)

    plt.title("??????????????????????????????[???]",fontproperties=fp,pad=13)
    plt.ylabel('???\n???\n???',fontproperties=fp_label, rotation=0, ha='center', labelpad=13)

    year = python_hours_array.iloc[-1].strftime("%Y") #take the year from the last date entry
    plt.xlabel('??????'+ year +'???',fontproperties=fp_label, labelpad=10)

    for label in ax.get_xticklabels():
        label.set_fontproperties(fp_xticklabel)

    for label in ax.get_yticklabels():
        label.set_fontproperties(fp_yticklabel)

    plt.rcParams.update({
        'font.size': 14,
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
    plt.grid(axis = 'x', color = 'grey', linewidth = 0.25)

    #outer margins are in percentages! keep them between 0 - 1 !!!:
    plt.tight_layout(rect=[graph_left_margin, graph_bottom_margin, graph_inner_width_in_onehundredth, graph_inner_height_in_onehundredth]) #, h_pad=0.2, w_pad=0.2

    plt.margins(x=0.03) #horizontal margins around the graph itself (the line with dots)    

    #saving
    tr = datetime.utcnow() + timedelta(milliseconds=0.5) #correct time rounding trick
    timestr = tr.strftime("%Y%m%d%H%M%S%f")[:-3]
    plt.savefig("./output/graph1_" + timestr + ".svg", format="svg", dpi=360)
    #plt.savefig("./output/graph1_" + timestr + ".png", format="png", dpi=360) #temporary PNG for easier preveiw for my client, use SVG for production!!!

    plt.show()

make_graph1()