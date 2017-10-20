import pandas as pd
import math

def findthesameinlist(seq):
  uniques = set()
  repeats = set()
  for a in [y for y in seq if str(y) != 'nan']:
    if a not in uniques:
      uniques.add(a)
    else:
      repeats.add(a)
  return list(repeats)

Location1 = r"N:\ServicePlanning\Signage Update\StopIDv28_RouteInfo.xlsx"
stops_df = pd.read_excel(Location1)

columnlinenames = ['Line 1','Line 2','Line 3','Line 4', 'Line 5', 'Line 6', 'Line 7', 'Line 8', 'Line 9', 'Line 10']
#columndirectionnames = ['Line 1 Direction', 'Line 2 Direction', 'Line 3 Direction', 'Line 4 Direction', 'Line 5 Direction', 'Line 6 Direction',
#'Line 7 Direction', 'Line 8 Direction', 'Line 9 Direction', 'Line 10 Direction']

#columnlines = stops_df.loc[:,columnlinenames]
#columndirections = stops_df.loc[:, columndirectionnames]

for x in range(len(stops_df)):
    stops_df.loc[x,'Potential Terminals'] = str(findthesameinlist(list(stops_df.loc[x,columnlinenames])))

Location2 = r"N:\ServicePlanning\Signage Update\TestFolder\StopIDv28_sample_terminals.xlsx"
stops_df.to_excel(Location2)
