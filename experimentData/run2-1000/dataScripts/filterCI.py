import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t.ppf((1 + confidence) / 2., n - 1)
    return -h, +h


# Read your data from file
plotly = "../plotly/diffs/org/plotly_org_filterDiff.txt"
plotly_df = pd.read_csv(plotly, header=None, names=['delta'])

d3_data = "../d3/diffs/org/d3_org_filterDiff.txt"
d3_df = pd.read_csv(d3_data, header=None, names=['delta'])

print("CI plotly delta: ", mean_confidence_interval(plotly_df['delta']))
print("CI custom delta: ", mean_confidence_interval(d3_df['delta']))

CI_delta = mean_confidence_interval(plotly_df['delta'])
CI_delta2 = mean_confidence_interval(d3_df['delta'])

# width of the bars
barWidth = 0.6

# Bars Data
barsData = [plotly_df['delta'].mean(), d3_df['delta'].mean()]
print(barsData)

# The x-position order of bars
# barsOrder = range(len(df.columns))
barsOrder = range(2)

# Std Bars Interval
# barsInterval = df.std()

# Bars for CI Intervals
df_CI = pd.DataFrame(list(zip(CI_delta, CI_delta2)), columns=['plotly', 'd3'])

barsInterval = df_CI.iloc[1]
print(barsInterval)

# Colours of bar charts
colors = ["orange", "purple"]

# Opacity of colours
Opacity = 0.5

# Start values from bottom of the bars
#minValue = int(min(df['delta']))
#print(minValue)

# Interval cap size
intervalCapsize = 0

# Plot bars
plt.bar(barsOrder, barsData, color=colors, edgecolor='black', width=barWidth,
        yerr=barsInterval, capsize=7, alpha=Opacity, bottom=intervalCapsize)

# Put a tick on the x-axis undex each bar and label it with column name
# plt.xticks(range(len(df.columns)), df.columns)

plt.ylabel('Load time in ms')
plt.yticks(range(0, 700, 50))
plt.xticks(range(2), ['Plotly', 'D3'])
plt.title('Filter Time Means Comparison for original GEI data')
plt.grid(False)
plt.savefig('../Graphs/filterLoadTimeDeltaOrg.png')
# plt.show()