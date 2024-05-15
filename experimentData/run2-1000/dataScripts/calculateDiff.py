import pandas as pd

start = "../d3/filterStartTimeD3.txt"
start_df = pd.read_csv(start, header=None, names=['epoch'])
end = "../d3/filterEndTimeD3.txt"
end_df = pd.read_csv(end, header=None, names=['epoch'])

delta = end_df['epoch'] - start_df['epoch']
for i in delta:
    print(i)

#bash this manually
#python3 calculateFilteringDiff.py > diffs/filename.txt