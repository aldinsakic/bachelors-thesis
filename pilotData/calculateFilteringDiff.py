import scipy.stats as stats
import numpy as np
import statsmodels.stats.multicomp as multi
import pandas as pd

d3filterStart = "pilotData/D3filterStartTime.txt"
d3filterStart_df = pd.read_csv(d3filterStart, header=None, names=['Epoch'])

print(d3filterStart_df)
