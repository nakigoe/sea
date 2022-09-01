#Three lines to make our compiler able to draw:
import sys
import matplotlib
#matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

sea = pd.read_csv('./input/raw_data.csv')

sea.plot()
plt.savefig("./output/test.svg", format="svg")
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

