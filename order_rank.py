import numpy as np
import pandas as pd


"""loads the ranks from csv files"""
ranks = pd.read_csv("CDLR/current_rank_2.csv")
ranks = ranks.sort_values(by="r", ascending=False)
ranks = pd.DataFrame({"t":ranks.loc[:,"t"].loc[:],"r":ranks.loc[:,"r"].loc[:],"rd":ranks.loc[:,"rd"].loc[:]})


"""Updates the current ranks csv file"""
ranks.to_csv("CDLR/current_rank_2.csv")


"""loads the ranks from csv files"""
ranks = pd.read_csv("CDLR/current_rank_2.csv")



change = pd.DataFrame({"x":range(12), "y":ranks.loc[:]["Unnamed: 0"]})
change["z"] = change["y"] - change["x"]
ranks = ranks.sort_values(by="r", ascending=False)
ranks = pd.DataFrame({"t":ranks.loc[:,"t"].loc[:],"r":ranks.loc[:,"r"].loc[:],"c":change.loc[:,"z"].loc[:],"rd":ranks.loc[:,"rd"].loc[:]})


"""Updates the current ranks csv file"""
ranks.to_csv("CDLR/current_rank_2.csv")
