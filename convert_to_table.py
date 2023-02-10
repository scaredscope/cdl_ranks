import numpy as np
import pandas as pd


"""loads the ranks from csv files"""
ranks = pd.read_csv("CDLR/current_rank_2.csv")


table = "Rank|Team|Score|Change\n--:|:--|:--|:--\n"
for i in range(len(ranks)):
    table = ''.join([table,str(i+1),"|",str(ranks.loc[:,"t"].loc[i]),"|",str(ranks.loc[:,"r"].loc[i])[:7],"|",str(ranks.loc[:,"c"].loc[i]),'\n'])
print(table)

ranks_table = open("CDLR/ranks_table.txt","w")
ranks_table.write(table)
ranks_table.close()
