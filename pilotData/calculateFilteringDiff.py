import pandas as pd

filterStart = "PlotlyfilterStartTime.txt"
filterStart_df = pd.read_csv(filterStart, header=None, names=['epoch'])
filterEnd = "PlotlyfilterEndTime.txt"
filterEnd_df = pd.read_csv(filterEnd, header=None, names=['epoch'])

delta = filterEnd_df['epoch'] - filterStart_df['epoch']
for i in delta:
    print(i)

#bash this manually
#python3 calculateFilteringDiff.py > diffs/filename.txt