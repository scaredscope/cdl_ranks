import numpy as np
import pandas as pd


"""loads the ranks from csv files"""
ranks = pd.read_csv("CDLR/current_rank_2.csv")


"""resets all ranks to 60"""
ranks = pd.DataFrame({"t":["ATLANTA FAZE", "CHICAGO HUNTSMEN", "DALLAS EMPIRE", "FLORIDA MUTINEERS", "LOS ANGELES GUERRILLAS", "OPTIC GAMING LOS ANGELES", "LONDON ROYAL RAVENS", "MINNESOTA ROKKR", "NEW YORK SUBLINERS", "PARIS LEGION", "SEATTLE SURGE", "TORONTO ULTRA"],"r":1500,"rd":350})


"""Updates the current ranks csv file"""
ranks.to_csv("CDLR/current_rank_2.csv")
