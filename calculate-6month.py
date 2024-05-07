# import csv
import pandas as pd 
import numpy as np 
# df = pd.DataFrame({ 
#     'A': [1, 2, np.nan, 4], 
#     'B': [5, np.nan, np.nan, 8], 
#     'C': [9, 10, 11, 12] 
# }) 
# df.interpolate() 
# for two rows with the same code and consecitive years, take a middle value between these. 
# because the list is ordered already in year, we can just take the next instance of a country code.

# the first 4, as in  2013, 2015, 2017, 2019 do not have years between them, here i will just take the year in between
# for all else its a 6 month value. 

# with open('modifiedheader.csv') as csvfile:
#     df = pd.read_csv(csvfile, sep=",", header=None, names=['year', 'code', 'value'])
#     for data in df:
#         print(data)
    # reader = csv.DictReader(csvfile)
    # for row in reader:
    #     if(row['code'] == 'SE'):
    #         print(row['year'], row['code'], row['value'])
    # instancesOfGivenCountry = 0
    # for row in reader:
    #     # if its the strange years, handle differently
    #     if(int(row['year']) < 2020):
    #         print(row)
        # else:
            # print(row)
    # df = pd.DataFrame({
    #     reader
    # })
    # print(df)
# take the first instance of a country appearing 
# when the same country comes up again, take the middle value base on the new instances year, 
# then store the new instances year and repeat. for every year and every instance. 
# if its  2013, 2015, 2017, 2019 dont do a middle value, just do middle year
# how do i do middle date of 2022, 2023 etc tho, 2022.5? and then change those later? 
        

# maybe start with transforming all the years into actual dates and then its ezpz to make it a 6 month or a middle year value.

# add the new values on the end, doenst matter. when comparing; only compare if its a whole year. 
# then for the quarters its only compare if the first instance is a whole and the next is a half. or two whole if there is no half.

# header 0 instead of None to delete the first row and assign names instead 
# https://stackoverflow.com/questions/51759122/difference-between-header-none-and-header-0-in-pandas
df = pd.read_csv("standardDateGEI.csv", sep=",", header=0, names=['group', 'variable', 'value'])
df2 = df
# to hold the new Dataframe rows to be added to the dataframe
newRows = []
for i in df.index:
    currentValue = df['value'][i]
    currentGroup = df['group'][i]
    orgDate = df['variable'][i]
    orgDateYear = orgDate[-4:]
    newDate = '1-6-' + orgDateYear
    # there is no 2023 noooo, because of -1?
    if (i < len(df['value'])-1) and (df['group'][i]==df['group'][i+1]):
        
        # print(df['variable'][i], df['value'][i])
        # orgDate = df['variable'][i]
        # print(orgDate)
        # slice so only the year remains, 1-1-2013 -> 2013
        # orgDateYear = orgDate[-4:]
        # print(orgDateYear)
        # newDate = '1-6-' + orgDateYear
        # print(newDate)

        # currentValue = df['value'][i]
        # currentGroup = df['group'][i]
        # print(currentValue)

        nextValue = df['value'][i+1]
        # print(df['variable'][i])

        # seems to work well, did manual comparison with the Plotly heatmap implementation
        # print(currentValue, nextValue, df['group'][i], df['group'][i+1])

        # close enough
        middleValue = currentValue+((nextValue-currentValue)/2)
        # print(round(middleValue,1))

        # print(newDate, df['group'][i], round(middleValue,1))
        # df.loc[i+0.5] = [newDate, df['group'][i], round(middleValue,1)]

        # https://stackoverflow.com/questions/15888648/is-it-possible-to-insert-a-row-at-an-arbitrary-position-in-a-dataframe-using-pan
        # line = pd.DataFrame({"group": 30.0, "variable": 1.3, "value": 1}, index=[i])
        # df2 = pd.concat([df.iloc[:i], line, df.iloc[i:]]).reset_index(drop=True)


        # its recursively taking the new values and using them for the calculations above, 
        # to get around this, ill store it all in an array and then do this after im out of this loop etc. in a new loop.
        # df.loc[i] = df['group'][i],newDate,round(middleValue,1)
        # df = df.sort_index().reset_index(drop=True)

        # based on https://stackoverflow.com/a/63736275
        newRows.append([df['group'][i],newDate,round(middleValue,1)])
    # for 2023
    else :
        # previous since there is no next
        previousValue = df['value'][i-1]
        middleValue = currentValue+((previousValue-currentValue)/2)
        # print(newDate, df['group'][i], round(middleValue,1))

        newRows.append([df['group'][i],newDate,round(middleValue,1)])


        # df.loc[1.5] = 'test'
        # print(df.loc([1]))
# print(df)
# print(len(newRows))
# df2 as to not have any operations affect the loop, check if its even needed
for i in df2.index:
    # if i < len(newRows):
    # if i%2==0:
        # if i < 1:
        df.loc[i+0.5] = newRows[round(i)]

    # for every other spot in df, take the top value from newRows, then delete this value. rinse and repeat until there is nothing left.
    # df.loc[i+0.5] = 
        
df = df.sort_index().reset_index(drop=True)
print(df.to_string())
        # if i+0.5 < len(df['value'])-1.5:
        #     df.loc[i+0.5] = [newDate, df['group'][i], round(middleValue,1)]
        # else:
        #     df.loc[-1] = [newDate, df['group'][i], round(middleValue,1)]

        # test1 = 80
        # test2 = 82
        # testMiddle = test1+((test2-test1)/2)
        # print(testMiddle)

    # in between lines, so i + 0.5
    #df.loc[i+.5] = [newDate, df['group'][i], idk]