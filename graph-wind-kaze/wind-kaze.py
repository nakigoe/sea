from svgmanip import Element
output = Element(1080, 720)  # size of the output file.

direction=90
direction=-direction #the app rotates clockwise, but we want counterclockwise rotation counting from the South (if the South in the coming data = 0)

base = Element('img/map.svg')
output.placeat(base, 0, 0)

marker_x = 100
marker_y = 150
wind = Element('img/wind.svg').scale(0.25).rotate(direction, 48, 20) #rotation point relative to the figure!!!
output.placeat(wind, marker_x, marker_y)

output.dump('output/output.svg')