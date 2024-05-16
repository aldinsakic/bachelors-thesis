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
    plotly = "../plotly/diffs/org/plotly_org_filterDiff.txt"
    plotly_df = pd.read_csv(plotly, header=None, names=['delta'])

    d3_data = "../d3/diffs/org/d3_org_filterDiff.txt"
    d3_df = pd.read_csv(d3_data, header=None, names=['delta'])
    # Run Anova on data groups
    if (anova(plotly_df['delta'], d3_df['delta'])):
        print("The means are different")
    else:
        print("No differences in means")


exampleAnova()