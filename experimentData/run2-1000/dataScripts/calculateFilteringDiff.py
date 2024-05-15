import pandas as pd

start = "D3initialTime.txt"
start_df = pd.read_csv(start, header=None, names=['epoch'])
end = "D3endTime.txt"
end_df = pd.read_csv(end, header=None, names=['epoch'])

delta = end_df['epoch'] - start_df['epoch']
for i in delta:
    print(i)

#bash this manually
#python3 calculateFilteringDiff.py > diffs/filename.txt