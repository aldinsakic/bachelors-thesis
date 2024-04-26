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
plotly = "PlotlyFilterDelta.txt"
plotly_df = pd.read_csv(plotly, header=None, names=['delta'])

d3_data = "D3FilterDelta.txt"
d3_df = pd.read_csv(d3_data, header=None, names=['delta'])

# since the experiment had a series of 5 standardized filtrations, it was deemed best to compare each filtration to its respective counterpart.
plotlyFilter1 = plotly_df.iloc[0::5]
plotlyFilter2 = plotly_df.iloc[1::5]
plotlyFilter3 = plotly_df.iloc[2::5]
plotlyFilter4 = plotly_df.iloc[3::5]
plotlyFilter5 = plotly_df.iloc[4::5]
D3Filter1 = d3_df.iloc[0::5]
D3Filter2 = d3_df.iloc[1::5]
D3Filter3 = d3_df.iloc[2::5]
D3Filter4 = d3_df.iloc[3::5]
D3Filter5 = d3_df.iloc[4::5]

print(plotlyFilter1,plotlyFilter2,plotlyFilter3,plotlyFilter4,plotlyFilter5)
print(D3Filter1,D3Filter2,D3Filter3,D3Filter4,D3Filter5)

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

plt.ylabel('Load delta in ms')
plt.yticks(range(0, 700, 50))
plt.xticks(range(2), ['plotly', 'D3'])
plt.title('Load-delta Means Comparison')
plt.grid(False)
plt.show()