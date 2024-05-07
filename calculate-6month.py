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

for i in df.index:
    # print(df['variable'][i], df['value'][i])
    orgDate = df['variable'][i]
    # print(orgDate)
    # slice so only the year remains, 1-1-2013 -> 2013
    orgDateYear = orgDate[-4:]
    # print(orgDateYear)
    newDate = '1-6-' + orgDateYear
    # print(newDate)

    currentValue = df['value'][i]
    # print(currentValue)

    # not sure why -1 is needed, without it it seems to go out of bounds on df
    # whatever tho, only last value doesnt exist but thats fine, ill manually calculate that one
    # TODO add to if, make sure its beneath 2023, lest i go over and start grabbing values from other countries
    if (i < len(df['value'])-1) and (df['group'][i]==df['group'][i+1]):
        nextValue = df['value'][i+1]
        print(df['variable'][i])

        # works well, did manual comparison with the Plotly heatmap implementation
        print(currentValue, nextValue, df['group'][i], df['group'][i+1])

    # in between lines, so i + 0.5
    #df.loc[i+.5] = [newDate, df['group'][i], idk]