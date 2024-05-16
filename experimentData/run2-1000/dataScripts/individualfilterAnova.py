import scipy.stats as stats
import numpy as np
import statsmodels.stats.multicomp as multi
import pandas as pd


def anova(*data):  # * indicates, 0, 1 , 2 .. arguments
    if len(data) == 2:
        statistic, pvalue = stats.f_oneway(data[0], data[1])
    elif len(data) == 3:
        statistic, pvalue = stats.f_oneway(data[0], data[1], data[2])
    elif len(data) == 4:
        statistic, pvalue = stats.f_oneway(data[0], data[1], data[2], data[3])
        print("ANOVA Statistic " + str(statistic) + " and p-value " + str(pvalue))
    if pvalue < statistic:
        print("ANOVA Statistic " + str(statistic) + " and p-value " + str(pvalue))
        return True
    else:
        print("ANOVA Statistic " + str(statistic) + " and p-value " + str(pvalue))
        return False


def exampleAnova():
    # Read your data from file
    plotly = "../plotly/diffs/exp/plotly_exp_filterDiff.txt"
    plotly_df = pd.read_csv(plotly, header=None, names=['delta'])

    d3_data = "../d3/diffs/exp/d3_exp_filterDiff.txt"
    d3_df = pd.read_csv(d3_data, header=None, names=['delta'])

    # plotlyFilter1 = plotly_df.iloc[0::5]
    # plotlyFilter2 = plotly_df.iloc[1::5]
    # plotlyFilter3 = plotly_df.iloc[2::5]
    # plotlyFilter4 = plotly_df.iloc[3::5]
    # plotlyFilter5 = plotly_df.iloc[4::5]
    # D3Filter1 = d3_df.iloc[0::5]
    # D3Filter2 = d3_df.iloc[1::5]
    # D3Filter3 = d3_df.iloc[2::5]
    # D3Filter4 = d3_df.iloc[3::5]
    # D3Filter5 = d3_df.iloc[4::5]
    # Run Anova on data groups
    # if (anova(plotly_df['delta'], d3_df['delta'])):
    #     print("The means are different")
    # else:
    #     print("No differences in means")
    for i in range(6):
        print(i)
        plotly_df.iloc[i::6]
        d3_df.iloc[i::6]
        if (anova(plotly_df.iloc[i::6]['delta'], d3_df.iloc[i::6]['delta'])):
            print("The means are different")
        else:
            print("No differences in means")


exampleAnova()