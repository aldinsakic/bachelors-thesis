import pandas as pd
import matplotlib.pyplot as plt

# Read your data from file
plotly = "PlotlyFilterDelta.txt"
d3 = "D3FilterDelta.txt"
plDf = pd.read_csv(plotly, header=None, names=['epoch'])
d3Df = pd.read_csv(d3, header=None, names=['epoch'])
# range from 0 to the length of the data, aka, amount of runs.
# x = range(0, len(df))
# y = df['Time'].tolist()  # because the following plot takes list of data
# searchWordXticks = df['SearchWord'].tolist()

x = range(0, 100)
PlY = plDf['epoch'].tolist()
d3Y = d3Df['epoch'].tolist()

# print(plDf['epoch'].mean())
# print(plDf['epoch'].std())
# print(d3Df['epoch'].mean())
# print(d3Df['epoch'].std())

# set the size of the graph, since the x ticks would be squished otherwise
# plt.figure(figsize=(9, 6), dpi=80)

# plt.plot(x, PlY)
# plt.plot(x, d3Y)

# for i in range(5):
#         print(i)
#         plt.plot(x, PlY[i::5])
#         plt.plot(x, d3Y[i::5])
#         # plt.plot(x, plDf.iloc[i::5]['epoch'].tolist())
#         # PlY.iloc[i::5]
#         # d3Y.iloc[i::5]
#         print(PlY[i::5])


# filter data, per each fitler since all filters at once was a visual mess and not very useful 
filters = [['BE'], ['DE'], ['BE', 'DK'], ['ES', 'CZ', 'EL', 'ES', 'FR', 'HR', 'IT', 'CY', 'LV', 'LT', 'LU', 'EE'], ['FI', 'SE', 'DK']]

for filter in filters:

    # whatever filter we are on i.e 1,2,3 etc. start counting every 5th from that in PlY and d3Y.
    plt.plot(x, PlY[filters.index(filter)::5], 'orange')
    plt.plot(x, d3Y[filters.index(filter)::5], 'purple')

    plt.ylim(ymin=0)
    plt.xlim(xmin=0, xmax=99)
    # -1 since we start from 0
    # plt.xlim(xmax=len(PlY[0::5]))

    plt.xticks(range(0,100,5))
    # range from 0 to the maximum value of y, with ticks of 50.
    plt.yticks(range(0, max(PlY), 50))

    # join the array so its string, not list 
    plt.title('Load time for filter '+(','.join(filter)))
    plt.xlabel('Run')
    plt.ylabel('Load time in ms')
    # plt.title('load-time for ' + str(len(df)) + ' runs')
    plt.grid(False)
    plt.legend(['Plotly', 'D3'])
    plt.savefig('../Graphs/filterLine'+str(filters.index(filter))+'.png')
    plt.show()