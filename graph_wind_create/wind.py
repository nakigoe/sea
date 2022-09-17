#code by Maxim Angel, email: teachermaxim@gmail.com
#You can see the latest version at https://github.com/nakigoe/sea/blob/main/graph_wind_create/wind.py

#------ basic usage ------ Python Library from https://github.com/CrazyPython/svgmanip
'''
output = Element(384, 356)  # size of the output file, look up the SVG code to get correct proportions!

map = Element('assets/map.svg')
marker = Element('assets/marker.svg').scale(size_in_one_hundredth).rotate(-degrees, x_rotation_center, y_rotation_center)
marker2 = Element('assets/marker2.svg').scale(0.5).rotate(-45, 50, 50)

output.placeat(map, 0, 0)
output.placeat(marker, 170.9, 0.08)
output.placeat(marker2, 100.9, 50)

output.dump('output.svg')
output.save_as_png('output.png', 1024) #does not work under Windows, utilize PYVIPS library and system PATH for PYVIPS DLLs
'''

# --------------------------- convert SVG to PNG under Windows: --------------------
# https://github.com/libvips/build-win64-mxe/releases
# unzip and add the BIN folder with DLL's to the system PATH
# comment this line out when moving the code for production, the only reason it's here is to create PNG files for easier preview in our team chat

import pyvips 

import pandas as pd
from svgmanip import Element 

def make_graph_wind():
    sea = pd.read_csv('input/raw_data.csv')
    marker_x=sea['x']
    marker_y=sea['y']
    direction=-sea['deg'] #the app rotates clockwise, but we want counterclockwise rotation counting from the South (if the South in the coming data = 0)

    #output file and graphics' placement
    output = Element(960, 700)  # size of the output file.

    base = Element('img/map.svg') #increase the map size directly inside the SVG file to Your liking!
    output.placeat(base, 0, 0) #place the map at the top left corner of the output SVG composed image

    wind_array=[]
    for i in range(len(sea.index)):
        wind = Element('img/wind.svg').scale(0.25).rotate(direction[i], 48, 20) #these numbers are marker's rotation points relative to the marker figure!!!
        wind_array.append(wind)
        output.placeat(wind_array[i], int(marker_x[i]), int(marker_y[i]))

    output.dump('output/output.svg')

    #comment the following section out when moving the code for production, it's here only to create PNG images for easier preview in our team chat:
    image = pyvips.Image.thumbnail("output/output.svg", 600)
    image.write_to_file("output/output.png")
   
make_graph_wind()