#code by Maxim Angel, email: teachermaxim@gmail.com
#You see the latest version at https://github.com/nakigoe/sea/blob/main/graph2_create/graph2.py

import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from cmath import rect

from datetime import datetime, timedelta
from matplotlib.font_manager import FontProperties

from matplotlib import collections as mc

def make_graph2():
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

    reveresd_sea = pd.read_csv('./input/raw_data.csv') #the original data comes in the reversed order, inverse:
    sea = reveresd_sea.iloc[::-1]

    #cmap = mpl.cm.plasma 
    direction = sea['向き[deg]'] #degrees start from the bottom (South) and increase counterclockwise. due South = 0. Therefore I subtract 90° from the data in a later section of the code when performing standard trigonometry operations!!!
    speed = sea['速さ[m/s]'] 
    timeline = sea['日時']

    #------------------------------- black border around the graph -----------------------------------
    fig = plt.figure(figsize=(total_width, total_height), linewidth=border_width, edgecolor="#000") 
    ax = fig.add_subplot()
    ax.axis('equal') #x and y axes are set here to have the same scale, in order to display the angles correctly
    ax.plot(timeline, np.zeros_like(timeline), "-o", color="k", lw=0.334, markerfacecolor="w")  # Baseline and markers on it.
        
    #-------------------------- x-axis formatting --------------------------
    x = pd.to_datetime(sea['日時'], format = '%Y/%m/%d %H:%M')
    total_hours = round((x.iloc[-1]-x.iloc[0]).total_seconds() / 3600)

    #plt.vlines(timeline, 0, speed, colors=['red','green','blue'], lw=5, alpha=0.5)  # The vertical stems.
    
    #--------------- get end point arrays based on speed and direction -----------------
    nprect = np.vectorize(rect)
    c = nprect(speed, np.deg2rad(direction-90)) #I am subtracting 90° from the direction, since the angles in the data start from the South!!!
    x_end = c.real
    y_end = c.imag

    #-------------------- waves speed and direction lines' array structure, by hand: ------------------
    #lines =[[(0, 0), (x_end[0], y_end[0])], 
    #        [(1, 0), (x_end[1]+1, y_end[1])], 
    #        [(2, 0), (x_end[2]+2, y_end[2])], 
    #        [(3, 0), (x_end[3]+3, y_end[3])], 
    #        [(4, 0), (x_end[4]+4, y_end[4])], 
    #        [(5, 0), (x_end[5]+5, y_end[5])], 
    #        [(6, 0), (x_end[6]+6, y_end[6])], 
    #        [(7, 0), (x_end[7]+7, y_end[7])], 
    #        [(8, 0), (x_end[8]+8, y_end[8])], 
    #        [(9, 0), (x_end[9]+9, y_end[9])], 
    #        [(10, 0), (x_end[10]+10, y_end[10])], 
    #        [(11, 0), (x_end[11]+11, y_end[11])], 
    #        [(12, 0), (x_end[12]+12, y_end[12])], 
    #        [(13, 0), (x_end[13]+13, y_end[13])], 
    #        [(14, 0), (x_end[14]+14, y_end[14])], 
    #        [(15, 0), (x_end[15]+15, y_end[15])], 
    #        [(16, 0), (x_end[16]+16, y_end[16])], 
    #        [(17, 0), (x_end[17]+17, y_end[17])], 
    #        [(18, 0), (x_end[18]+18, y_end[18])], 
    #        [(19, 0), (x_end[19]+19, y_end[19])], 
    #        [(20, 0), (x_end[20]+20, y_end[20])], 
    #        [(21, 0), (x_end[21]+21, y_end[21])], 
    #        [(22, 0), (x_end[22]+22, y_end[22])], 
    #        [(23, 0), (x_end[23]+23, y_end[23])]]

    #an automated alternative to accommodate any amount of hourly data:        
    lines_array = []
    for i in range(total_hours+1):
        line=((i, 0), (x_end[i]+i, y_end[i])) # x0 = i, y0 = 0, add i to the x[i] from the iteration over the lines to receive the real x coordinate for each end point, that is x_end[i] = i + x[i]
        lines_array.append(line)

    c = np.array([(1, 0, 0, 0.75), (0, 1, 0, 0.75), (0, 0, 1, 0.75)]) #colors with opacity 0.75 to see the graph even when the lines overlap
    lc = mc.LineCollection(lines_array, colors=c, linewidths=5)
    ax.add_collection(lc)

    # Show the right and top spines
    ax.spines.right.set_visible(True)
    ax.spines.top.set_visible(True)

    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    ax.xaxis_date()
    xstart = 0
    xend=total_hours
    ax.xaxis.set_ticks(np.arange(xstart, xend+1, 1))
    ax.set_xticklabels(sea['日時'].str[5:].str.replace(' ','\n')) #an alternative is to rotate 45 deg and to use: .str.replace('/','月').str.replace(' ','日\n'))
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

    #---------------- y ticks start and end position -----------------
    yabs_max = abs(max(ax.get_ylim(), key=abs))
    end = 1.2*yabs_max # a request from the client to increase the grid limit to 1.2 of the original value
    ax.set_ylim(ymin=-end, ymax=end)

    #ax.yaxis.set(major_locator=mpl.ticker.MultipleLocator(celsius_distance))
    #end = math.ceil(end * 2) / 2 #another request from the client to round to the nearest half
    #ax.yaxis.set_ticks(np.arange(-end, end, 2))
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))

    # Disjoin bottom / left spines by moving them outwards
    #for s in ['bottom', 'left']: ax.spines[s].set_position(('outward', 12))

    #font formatting:
    fp_xticklabel=FontProperties(family=['Sans-Serif','Arial', 'Verdana','Helvetica'], weight='semibold', size=12)
    fp_yticklabel=FontProperties(family=['Sans-Serif', 'Arial', 'Verdana','Helvetica'], weight='semibold', size=12)
    #Just in case the Japanese font 'MS Gothic' is not installed on the system, grab it from the SEA root folder:
    fp = FontProperties(fname='../fonts/msgothic.ttc', size=19)
    fp_label = FontProperties(fname='../fonts/msgothic.ttc', size=16)

    plt.title("高知県の水産業の海の波の向きと大きさ",fontproperties=fp,pad=13)
    plt.ylabel('▲\nN',fontproperties=fp_label, rotation=0, ha='center', labelpad=13)

    year = x.iloc[-1].strftime("%Y")
    plt.xlabel('日時'+ year +'年',fontproperties=fp_label, labelpad=10)

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

    #plt.grid(axis = 'y', color = 'grey', linewidth = 0.334)
    plt.grid(axis = 'x', color = 'grey', linewidth = 0.25)

    #outer margins are in percentages! keep them between 0 - 1 !!!:
    plt.tight_layout(rect=[graph_left_margin, graph_bottom_margin, graph_inner_width_in_onehundredth, graph_inner_height_in_onehundredth]) #, h_pad=0.2, w_pad=0.2

    plt.margins(x=0.03) #horizontal margins around the graph itself (the line with dots)    

    #saving
    tr = datetime.utcnow() + timedelta(milliseconds=0.5) #correct time rounding trick
    timestr = tr.strftime("%Y%m%d%H%M%S%f")[:-3]
    plt.savefig("./output/graph2_" + timestr + ".svg", format="svg", dpi=360)
    #plt.savefig("./output/graph2_" + timestr + ".png", format="png", dpi=360) #temporary PNG for easier preveiw for my client, use SVG for production!!!

    plt.show()

make_graph2()