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

print("CI plotly filter 1: ", mean_confidence_interval(plotlyFilter1['delta']))
print("CI plotly filter 2: ", mean_confidence_interval(plotlyFilter2['delta']))
print("CI plotly filter 3: ", mean_confidence_interval(plotlyFilter3['delta']))
print("CI plotly filter 4: ", mean_confidence_interval(plotlyFilter4['delta']))
print("CI plotly filter 5: ", mean_confidence_interval(plotlyFilter5['delta']))
print("CI D3 filter 1: ", mean_confidence_interval(D3Filter1['delta']))
print("CI D3 filter 2: ", mean_confidence_interval(D3Filter2['delta']))
print("CI D3 filter 3: ", mean_confidence_interval(D3Filter3['delta']))
print("CI D3 filter 4: ", mean_confidence_interval(D3Filter4['delta']))
print("CI D3 filter 5: ", mean_confidence_interval(D3Filter5['delta']))

plotlyFilter1_CI = mean_confidence_interval(plotlyFilter1['delta'])
plotlyFilter2_CI = mean_confidence_interval(plotlyFilter2['delta'])
plotlyFilter3_CI = mean_confidence_interval(plotlyFilter3['delta'])
plotlyFilter4_CI = mean_confidence_interval(plotlyFilter4['delta'])
plotlyFilter5_CI = mean_confidence_interval(plotlyFilter5['delta'])
D3Filter1_CI = mean_confidence_interval(D3Filter1['delta'])
D3Filter2_CI = mean_confidence_interval(D3Filter2['delta'])
D3Filter3_CI = mean_confidence_interval(D3Filter3['delta'])
D3Filter4_CI = mean_confidence_interval(D3Filter4['delta'])
D3Filter5_CI = mean_confidence_interval(D3Filter5['delta'])


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
            plotlyFilter5['delta'].mean()
            ]
D3BarsData = [D3Filter1['delta'].mean(), 
            D3Filter2['delta'].mean(), 
            D3Filter3['delta'].mean(),
            D3Filter4['delta'].mean(),
            D3Filter5['delta'].mean()
            ]
# print(barsData)

# The x-position order of bars
# barsOrder = range(len(df.columns))
# barsOrder = range(10)
barsOrder = np.arange(5)

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
                              )), columns=['plotlyfilter1','plotlyfilter2','plotlyfilter3','plotlyfilter4','plotlyfilter5'])
D3_df_CI = pd.DataFrame(list(zip(D3Filter1_CI, 
                              D3Filter2_CI,
                              D3Filter3_CI,
                              D3Filter4_CI,
                              D3Filter5_CI,
                              )), columns=['D3filter1','D3filter2','D3filter3','D3filter4','D3filter5'])

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

plt.ylabel('Load time delta in ms')
plt.yticks(range(0, 700, 50))
plt.xticks(range(5), ['BE', 'DE','BE & DK', 'ES, CZ, EL, ES, FR, HR, IT, CY, LV, LT, LU & EE', 'FI, SE & DK'])
plt.title('Individual Filters Time Delta Means Comparison')
plt.legend(["Plotly", "D3"]) 
plt.grid(False)
# bbox tight removes white margin on the image
plt.savefig('../Graphs/IndividualFilterLoadTimeDelta.png', bbox_inches='tight')
# plt.show()