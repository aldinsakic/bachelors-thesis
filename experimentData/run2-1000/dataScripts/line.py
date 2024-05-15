import pandas as pd
import matplotlib.pyplot as plt

# Read your data from file
plotly = "plotlyLoadDelta.txt"
d3 = "D3LoadDelta.txt"
plDf = pd.read_csv(plotly, header=None, names=['epoch'])
d3Df = pd.read_csv(d3, header=None, names=['epoch'])
# range from 0 to the length of the data, aka, amount of runs.
# x = range(0, len(df))
# y = df['Time'].tolist()  # because the following plot takes list of data
# searchWordXticks = df['SearchWord'].tolist()

x = range(0, len(plDf))
PlY = plDf['epoch'].tolist()
d3Y = d3Df['epoch'].tolist()

print(plDf['epoch'].mean())
print(plDf['epoch'].std())
print(d3Df['epoch'].mean())
print(d3Df['epoch'].std())

# set the size of the graph, since the x ticks would be squished otherwise
# plt.figure(figsize=(18, 6), dpi=80)

plt.plot(x, PlY, 'orange')
plt.plot(x, d3Y, 'purple')

plt.ylim(ymin=0)
plt.xlim(xmin=0, xmax=99)


plt.xticks(range(0,100,5))
# range from 0 to the maximum value of y, with ticks of 50.
plt.yticks(range(0, max(PlY), 50))

plt.xlabel('Run')
plt.ylabel('Load time in ms')
# plt.title('load-time for ' + str(len(df)) + ' runs')
plt.title('Load time mean time')
plt.grid(False)
plt.legend(['Plotly', 'D3'])
plt.savefig('../Graphs/loadTimeDeltaLine.png', bbox_inches='tight')
plt.show()