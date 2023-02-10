import numpy as np
import pandas as pd


"""loads the ranks and results from csv files"""
results = pd.read_csv("CDLR/results.csv")
ranks = pd.read_csv("CDLR/current_rank_2.csv")


"""Defining some functions and variables"""
q = np.log(10)/400

def g(RDi):
    global q
    return 1 / (np.sqrt(1 + (3 * float(q**2) * RDi**(2)) / np.pi**2))

def E(s,r0,ri,RDi):
    return 1 / (1 + 10**(( g(RDi) * (r0 - ri)) / -400))


for i in range(len(results)):
    """finds both teams current rank, RD and the result of the match"""
    r0 = float(ranks.loc[ranks.t == results.loc[i,"a"]].r)
    ri = float(ranks.loc[ranks.t == results.loc[i,"b"]].r)
    RD0 = float(ranks.loc[ranks.t == results.loc[i,"a"]].rd)
    RDi = float(ranks.loc[ranks.t == results.loc[i,"b"]].rd)
    s = results.loc[i,"s"]
    print(r0,ri,RD0,RDi,s)
    
    """Updates rank & RD of the first team"""
    dsq = 1 / (float(q**2) * g(RDi)**2 * E(s, r0, ri, RDi) * (1 - E(s, r0, ri, RDi)))
    r = r0 + (q / ((1/RD0**2) + (1/dsq))) * g(RDi) * (s - E(s, r0, ri, RDi))
    ranks.loc[ranks.loc[ranks.t == results.loc[i,"a"]].index,"r"] = r
    RD = np.sqrt(((1 / RD0**2) + (1 / dsq))**-1)
    ranks.loc[ranks.loc[ranks.t == results.loc[i,"a"]].index,"rd"] = RD


    """Updates rank & RD of the second team"""
    s = 1 - s
    dsq = 1 / (float(q**2) * g(RD0)**2 * E(s, ri, r0, RD0) * (1 - E(s, ri, r0, RD0)))
    r = ri + (q / ((1/RDi**2) + (1/dsq))) * g(RD0) * (s - E(s, ri, r0, RD0))    
    ranks.loc[ranks.loc[ranks.t == results.loc[i,"b"]].index,"r"] = r
    RD = np.sqrt(((1 / RD0**2) + (1 / dsq))**-1)
    ranks.loc[ranks.loc[ranks.t == results.loc[i,"b"]].index,"rd"] = RD


"""Updates the current ranks csv file"""
ranks = pd.DataFrame({"t":ranks.loc[:,"t"].loc[:],"r":ranks.loc[:,"r"].loc[:],"rd":ranks.loc[:,"rd"].loc[:]})
ranks.to_csv("CDLR/current_rank_2.csv")
