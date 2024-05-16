import pandas as pd
import matplotlib.pyplot as plt

# Read your data from file
plotly = "../plotly/diffs/org/plotly_org_filterDiff.txt"
d3 = "../d3/diffs/org/d3_org_filterDiff.txt"
plDf = pd.read_csv(plotly, header=None, names=['epoch'])
d3Df = pd.read_csv(d3, header=None, names=['epoch'])
# range from 0 to the length of the data, aka, amount of runs.
# x = range(0, len(df))
# y = df['Time'].tolist()  # because the following plot takes list of data
# searchWordXticks = df['SearchWord'].tolist()

x = range(0, 6000)
PlY = plDf['epoch'].tolist()
d3Y = d3Df['epoch'].tolist()

# print(plDf['epoch'].mean())
# print(plDf['epoch'].std())
# print(d3Df['epoch'].mean())
# print(d3Df['epoch'].std())

# set the size of the graph, since the x ticks would be squished otherwise
plt.figure(figsize=(18, 6), dpi=80)

plt.plot(x, PlY, 'orange')
plt.plot(x, d3Y, 'purple')

plt.ylim(ymin=0)
plt.xlim(xmin=0, xmax=5999)


plt.xticks(range(0,6000,200))
# range from 0 to the maximum value of y, with ticks of 50.
plt.yticks(range(0, max(PlY), 50))

plt.xlabel('Run')
plt.ylabel('Load time in ms')
# plt.title('load-time for ' + str(len(df)) + ' runs')
plt.title('Load time mean time in ms across all 5 filtrations for the orgiginal GEI data')
plt.grid(False)
plt.legend(['Plotly', 'D3'])
plt.savefig('../Graphs/allFilterMeanOrg.png', bbox_inches='tight')
plt.show()

# for i in range(5):
#         print(i)
#         plt.plot(x, PlY[i::5])
#         plt.plot(x, d3Y[i::5])
#         # plt.plot(x, plDf.iloc[i::5]['epoch'].tolist())
#         # PlY.iloc[i::5]
#         # d3Y.iloc[i::5]
#         print(PlY[i::5])


# filter data, per each fitler since all filters at once was a visual mess and not very useful 
# filters = [['BE'], ['DE'], ['BE', 'DK'], ['ES', 'CZ', 'EL', 'ES', 'FR', 'HR', 'IT', 'CY', 'LV', 'LT', 'LU', 'EE'], ['FI', 'SE', 'DK']]

# for filter in filters:

#     # whatever filter we are on i.e 1,2,3 etc. start counting every 5th from that in PlY and d3Y.
#     plt.plot(x, PlY[filters.index(filter)::5], 'orange')
#     plt.plot(x, d3Y[filters.index(filter)::5], 'purple')

#     # + 100 to make room for the legend
#     plt.ylim(ymin=0, ymax=max(PlY)+100)
#     plt.xlim(xmin=0, xmax=99)
#     # -1 since we start from 0
#     # plt.xlim(xmax=len(PlY[0::5]))

#     plt.xticks(range(0,100,5))
#     # range from 0 to the maximum value of y, with ticks of 50.
#     plt.yticks(range(0, max(PlY), 50))

#     # join the array so its string, not list 
#     # plt.figure(figsize=(8, 8), dpi=80)
#     plt.title('Load time for filter '+(','.join(filter)))
#     plt.xlabel('Run')
#     plt.ylabel('Load time in ms')
#     # plt.title('load-time for ' + str(len(df)) + ' runs')
#     plt.grid(False)
#     plt.legend(['Plotly', 'D3'])
#     plt.savefig('../Graphs/filterLine'+str(filters.index(filter))+'.png', bbox_inches='tight')
#     plt.show()