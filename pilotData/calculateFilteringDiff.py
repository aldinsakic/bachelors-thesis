import pandas as pd

filterStart = "pilotData/D3filterStartTime.txt"
filterStart_df = pd.read_csv(filterStart, header=None, names=['epoch'])
filterEnd = "pilotData/D3filterEndTime.txt"
filterEnd_df = pd.read_csv(filterEnd, header=None, names=['epoch'])

delta = filterEnd_df['epoch'] - filterStart_df['epoch']
for i in delta:
    print(i)

#bash this manually
#python3 pilotData/calculateFilteringDiff.py > file.txt