"""
complex_problem16:

Write a Pandas Program To Add Some Data To An Existing Series. 

"""

import pandas as pd

ps = pd.Series([1,2,3,4,5,6])
print(ps)
ps_updated = ps.append(pd.Series([7,8,9]))
print(ps_updated)



# # if append not work use concat
# import pandas as pd

# ps = pd.Series([1,2,3,4,5,6])
# print(ps)
# ps_updated = pd.concat([ps, pd.Series([7,8,9])])
# print(ps_updated)
