import numpy as np
import pandas as pd

ranks = pd.read_csv("CDLR/current_rank.csv")
print(ranks)
print(ranks.loc[:]["Unnamed: 0"])