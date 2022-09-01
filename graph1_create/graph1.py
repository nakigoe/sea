#Three lines to make our compiler able to draw:
import sys
import matplotlib
import time
from datetime import datetime, timedelta
#matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

sea = pd.read_csv('./input/raw_data.csv')

sea.plot()

#saving
tr = datetime.utcnow() + timedelta(milliseconds=0.5) #correct time rounding trick
timestr = tr.strftime("%Y%m%d%H%M%S%f")[:-3]
plt.savefig("./output/graph1_" + timestr + ".svg", format="svg")

#comment the following section out when moving the project to production:
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
