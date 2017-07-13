import pandas as pd

Location1 = r''
Location2 = r''
stops_df = pd.read_excel(Location1)
reference_df = pd.read_excel(Location2)

columnlinenames = ['Line 1','Line 2','Line 3','Line 4', 'Line 5', 'Line 6', 'Line 7', 'Line 8', 'Line 9', 'Line 10', 'Line 11', 'Line 12', 'Line 13']

reference_list = set(reference_dict['route'].tolist)
reference_dict = {}

for j in range(len(reference_df)):
  reference_dict[reference_df.loc[j, 'Stop ID']] = reference_dict.loc[j,'category']

for ind in range(7,len(stops_df)):
  for name in columnlinenames:
    if stops_df.loc[ind,name] =
