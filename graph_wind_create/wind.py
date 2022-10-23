'''
code by Maxim Angel, email: teachermaxim@gmail.com
You can see the latest version at https://github.com/nakigoe/sea/blob/main/graph_wind_create/wind.py

------------------------------------ basic usage ---------------------------------- 
Python Library from https://github.com/CrazyPython/svgmanip

output = Element(384, 356)  # size of the output file, look up the SVG code to get correct proportions!

map = Element('assets/map.svg')
marker = Element('assets/marker.svg').scale(size_in_one_hundredth).rotate(-degrees, x_rotation_center, y_rotation_center)
marker2 = Element('assets/marker2.svg').scale(0.5).rotate(-45, 50, 50)

output.placeat(map, 0, 0)
output.placeat(marker, 170.9, 0.08)
output.placeat(marker2, 100.9, 50)

output.dump('output.svg')
output.save_as_png('output.png', 1024) #does not work under Windows, utilize PYVIPS library and system PATH for PYVIPS DLLs

************************************** convert SVG to PNG *********************************************************

=============================== Install Libvips under Windows: =====================================
https://github.com/libvips/build-win64-mxe/releases
unzip and add the BIN folder with DLL's to the system PATH

=============================== Install Libvips in Red Hat Enterprise Linux 9 ======================
-------------------------------------- Setup Python ----------------------------------------
$ su root
# dnf install python-requests
# dnf install python-pip
# dnf install python-wheel

-------------------------------------- Install Libvips ----------------------------------------
# subscription-manager repos --enable codeready-builder-for-rhel-9-x86_64-rpms
# subscription-manager repos --enable codeready-builder-for-rhel-9-$(arch)-rpms
# dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
# dnf install https://rpms.remirepo.net/enterprise/remi-release-9.rpm
# dnf config-manager --set-enabled remi
# dnf install vips vips-devel vips-tools
# dnf upgrade

--------------------------------- Install the app dependencies -------------------------------
$ pip install pyvips
$ pip install pandas
$ pip install svgutils

-------------------------------------- Run the wind.py app -------------------------------------
$ python wind.py
'''
import pyvips 

import pandas as pd
from svgmanip import Element 

def make_graph_wind():
    #!!! YOU HAVE TO SET THE WIDTH AND HEIGHT PROPERTIES to 100% INSIDE ALL SVG FILES MANUALLY IF THESE TWO PROPERTIES ARE ABSENT INSIDE SVG FILES' HEADERS!!!
    original_map_width = 535 #532.1  #SVG hardcoded numbers, open the SVG file!
    original_map_height = 431 #417.6 
    map_scale_up = 2 #increase the output dimensions to your liking by this parameter!
    map_width = original_map_width * map_scale_up #PNG 1070px
    map_height = original_map_height * map_scale_up
    
    sea = pd.read_csv('input/raw_data.csv')
    marker_x = map_width * sea['x']
    marker_y = map_height * sea['y']
    direction = -sea['deg'] #the app rotates clockwise, but we want counterclockwise rotation counting from the South (if the South in the coming data = 0)
    
    #output file and graphics' placement
    output = Element(map_width, map_height)  # size of the output file. 

    base = Element('img/map.svg').scale(map_scale_up)
    output.placeat(base, 0, 0) #place the map at the top left corner of the output SVG composed image

    wind_array=[]
    for i in range(len(sea.index)):
        wind = Element('img/wind.svg').scale(0.1667*map_scale_up).rotate(direction[i], 44.715225, 18.5) #these numbers are marker's rotation points relative to the marker figure, open SVG to see its size, multiply width by 0.5, height by 0.12 to get these relative rotation coordinates!!!
        wind_array.append(wind)
        output.placeat(wind_array[i], marker_x[i], marker_y[i])
    
    output.dump('output/output.svg')

    image = pyvips.Image.thumbnail("output/output.svg", map_width)
    image.write_to_file("output/output.png")
   
make_graph_wind()