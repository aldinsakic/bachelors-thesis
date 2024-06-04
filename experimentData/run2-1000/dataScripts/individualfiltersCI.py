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
plotly = "../plotly/diffs/exp/plotly_exp_filterDiff.txt"
plotly_df = pd.read_csv(plotly, header=None, names=['delta'])

d3_data = "../d3/diffs/exp/d3_exp_filterDiff.txt"
d3_df = pd.read_csv(d3_data, header=None, names=['delta'])

# since the experiment had a series of 6 standardized filtrations, it was deemed best to compare each filtration to its respective counterpart.
plotlyFilter1 = plotly_df.iloc[0::6]
plotlyFilter2 = plotly_df.iloc[1::6]
plotlyFilter3 = plotly_df.iloc[2::6]
plotlyFilter4 = plotly_df.iloc[3::6]
plotlyFilter5 = plotly_df.iloc[4::6]
plotlyFilter6 = plotly_df.iloc[5::6]
D3Filter1 = d3_df.iloc[0::6]
D3Filter2 = d3_df.iloc[1::6]
D3Filter3 = d3_df.iloc[2::6]
D3Filter4 = d3_df.iloc[3::6]
D3Filter5 = d3_df.iloc[4::6]
D3Filter6 = d3_df.iloc[5::6]

print(plotlyFilter1,plotlyFilter2,plotlyFilter3,plotlyFilter4,plotlyFilter5,plotlyFilter6)
print(D3Filter1,D3Filter2,D3Filter3,D3Filter4,D3Filter5,D3Filter6)

# print("CI plotly filter 1: ", mean_confidence_interval(plotlyFilter1['delta']))
# print("CI plotly filter 2: ", mean_confidence_interval(plotlyFilter2['delta']))
# print("CI plotly filter 3: ", mean_confidence_interval(plotlyFilter3['delta']))
# print("CI plotly filter 4: ", mean_confidence_interval(plotlyFilter4['delta']))
# print("CI plotly filter 5: ", mean_confidence_interval(plotlyFilter5['delta']))
# print("CI D3 filter 1: ", mean_confidence_interval(D3Filter1['delta']))
# print("CI D3 filter 2: ", mean_confidence_interval(D3Filter2['delta']))
# print("CI D3 filter 3: ", mean_confidence_interval(D3Filter3['delta']))
# print("CI D3 filter 4: ", mean_confidence_interval(D3Filter4['delta']))
# print("CI D3 filter 5: ", mean_confidence_interval(D3Filter5['delta']))

plotlyFilter1_CI = mean_confidence_interval(plotlyFilter1['delta'])
plotlyFilter2_CI = mean_confidence_interval(plotlyFilter2['delta'])
plotlyFilter3_CI = mean_confidence_interval(plotlyFilter3['delta'])
plotlyFilter4_CI = mean_confidence_interval(plotlyFilter4['delta'])
plotlyFilter5_CI = mean_confidence_interval(plotlyFilter5['delta'])
plotlyFilter6_CI = mean_confidence_interval(plotlyFilter6['delta'])
D3Filter1_CI = mean_confidence_interval(D3Filter1['delta'])
D3Filter2_CI = mean_confidence_interval(D3Filter2['delta'])
D3Filter3_CI = mean_confidence_interval(D3Filter3['delta'])
D3Filter4_CI = mean_confidence_interval(D3Filter4['delta'])
D3Filter5_CI = mean_confidence_interval(D3Filter5['delta'])
D3Filter6_CI = mean_confidence_interval(D3Filter6['delta'])


# CI_delta = mean_confidence_interval(plotly_df['delta'])
# CI_delta2 = mean_confidence_interval(d3_df['delta'])

# width of the bars
barWidth = 0.2

# Bars Data
# barsData = [plotlyFilter1['delta'].mean(), D3Filter1['delta'].mean(), 
#             plotlyFilter2['delta'].mean(), D3Filter2['delta'].mean(), 
#             plotlyFilter3['delta'].mean(), D3Filter3['delta'].mean(),
#             plotlyFilter4['delta'].mean(), D3Filter4['delta'].mean(),
#             plotlyFilter5['delta'].mean(), D3Filter5['delta'].mean()
#             ]
PlotlyBarsData = [plotlyFilter1['delta'].mean(), 
            plotlyFilter2['delta'].mean(), 
            plotlyFilter3['delta'].mean(),
            plotlyFilter4['delta'].mean(),
            plotlyFilter5['delta'].mean(),
            plotlyFilter6['delta'].mean()
            ]
D3BarsData = [D3Filter1['delta'].mean(), 
            D3Filter2['delta'].mean(), 
            D3Filter3['delta'].mean(),
            D3Filter4['delta'].mean(),
            D3Filter5['delta'].mean(),
            D3Filter6['delta'].mean()
            ]
# print(barsData)

# The x-position order of bars
# barsOrder = range(len(df.columns))
# barsOrder = range(10)
barsOrder = np.arange(6)

# Std Bars Interval
# barsInterval = df.std()

# Bars for CI Intervals
# df_CI = pd.DataFrame(list(zip(plotlyFilter1_CI, D3Filter1_CI, 
#                               plotlyFilter2_CI, D3Filter2_CI,
#                               plotlyFilter3_CI, D3Filter3_CI,
#                               plotlyFilter4_CI, D3Filter4_CI,
#                               plotlyFilter5_CI, D3Filter5_CI,
#                               )), columns=['plotlyfilter1', 'd3filter1',
#                                            'plotlyfilter2', 'd3filter2',
#                                            'plotlyfilter3', 'd3filter3',
#                                            'plotlyfilter4', 'd3filter4',
#                                            'plotlyfilter5', 'd3filter5',])
plotly_df_CI = pd.DataFrame(list(zip(plotlyFilter1_CI, 
                              plotlyFilter2_CI,
                              plotlyFilter3_CI,
                              plotlyFilter4_CI,
                              plotlyFilter5_CI,
                              plotlyFilter6_CI,
                              )), columns=['plotlyfilter1','plotlyfilter2','plotlyfilter3','plotlyfilter4','plotlyfilter5','plotlyfilter6'])
D3_df_CI = pd.DataFrame(list(zip(D3Filter1_CI, 
                              D3Filter2_CI,
                              D3Filter3_CI,
                              D3Filter4_CI,
                              D3Filter5_CI,
                              D3Filter6_CI,
                              )), columns=['D3filter1','D3filter2','D3filter3','D3filter4','D3filter5','D3filter6'])

# barsInterval = df_CI.iloc[1]
PlotlybarsInterval = plotly_df_CI.iloc[1]
# print(PlotlybarsInterval)
D3barsInterval = D3_df_CI.iloc[1]
# print(D3barsInterval)

# Colours of bar charts
# colors = ["orange", "purple"]

# Opacity of colours
Opacity = 0.5

# Start values from bottom of the bars
#minValue = int(min(df['delta']))
#print(minValue)

# Interval cap size
intervalCapsize = 0

# Plot bars
# plt.bar(barsOrder, barsData, color=colors, edgecolor='black', width=barWidth,
#         yerr=barsInterval, capsize=7, alpha=Opacity, bottom=intervalCapsize)

# set a fig size to always have the window be this size.
plt.figure(figsize=(15,6))

plt.bar(barsOrder-0.1, PlotlyBarsData, color="orange", edgecolor='black', width=barWidth,
        yerr=PlotlybarsInterval, capsize=7, alpha=Opacity, bottom=intervalCapsize)
plt.bar(barsOrder+0.1, D3BarsData, color="purple", edgecolor='black', width=barWidth,
        yerr=D3barsInterval, capsize=7, alpha=Opacity, bottom=intervalCapsize)

# Put a tick on the x-axis undex each bar and label it with column name
# plt.xticks(range(len(df.columns)), df.columns)
# [['BE'], ['FI'], ['FI', 'DK'], ['BE', 'DK'], ['BE', 'DK', 'SE', 'IT'], ['FI', 'DK', 'SE', 'IT']]
# 'BE, FI, FI & DK, BE & DK, BE DK SE & IT, FI DK SE & IT']

plt.ylabel('Load time in ms')
plt.yticks(range(0, 700, 50))
plt.xticks(range(6), ['BE','FI','FI & DK','BE & DK','BE DK SE & IT','FI DK SE & IT'])
plt.title('Individual Filters Time Means Comparison for Expanded GEI data')
plt.legend(["Plotly", "D3"]) 
plt.grid(False)
# bbox tight removes white margin on the image
plt.savefig('../Graphs/IndividualFilterLoadTimeDeltaExp.png', bbox_inches='tight')
# plt.show()