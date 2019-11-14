import numpy as np
import pandas as pd


"""loads the ranks and results from csv files"""
results = pd.read_csv("CDLR/results.csv")
ranks = pd.read_csv("CDLR/current_rank.csv")


def match(a,b,s):
    """finds the amount of points exchanged in each match"""
    if s == 0:
        x = 0
    else:
        d = a - b
        if d >= 10:
            d = 10
        elif d <= -10:
            d = -10
        x = -1*(((d)*0.1) - s)

    return x


for i in range(len(results)):
    """finds both teams current rank and the result of the match"""
    a = float(ranks.loc[ranks.t == results.loc[i,"a"]].r)
    b = float(ranks.loc[ranks.t == results.loc[i,"b"]].r)
    s = results.loc[i,"s"]
    
    """the winning team takes points from the loosing team"""
    c = match(a,b,s)
    a = a + c
    b = b - c

    """Updates the ranks dataframe with the new values"""
    ranks.loc[ranks.loc[ranks.t == results.loc[i,"a"]].index,"r"] = a
    ranks.loc[ranks.loc[ranks.t == results.loc[i,"b"]].index,"r"] = b


"""Updates the current ranks csv file"""
ranks = pd.DataFrame({"t":ranks.loc[:,"t"].loc[:],"r":ranks.loc[:,"r"].loc[:]})
ranks.to_csv("CDLR/current_rank.csv")
