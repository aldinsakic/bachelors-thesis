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

df = pd.read_csv("modifiedheader.csv", sep=",", header=None, names=['year', 'code', 'value'])
for data in df:
    print(df[data])