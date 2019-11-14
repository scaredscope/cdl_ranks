import numpy as np
import pandas as pd


"""loads the ranks from csv files"""
ranks = pd.read_csv("CDLR/current_rank.csv")


"""resets all ranks to 60"""
ranks = pd.DataFrame({"t":["ATL","CHI","DAL","FLO","LAG","LAO","LDN","MIN","NYS","PAR","SEA","TOR"],"r":60})


"""Updates the current ranks csv file"""
ranks.to_csv("CDLR/current_rank.csv")