import pandas as pd
import numpy as np

Metro = ['J', 'K', 'L', 'M', 'N', 'T']
Historic = ['E', 'F', 59]
Rapid = ['5R', '9R', '14R', '28R', '38R']
Frequentlocal = [1, 7, 8, 9, 14, 22, 28, 30, 38, 47, 49]
Grid = [2, 3, 5, 6, 10, 12, 18, 19, 21, 23, 24, 27, 29, 31, 33, 43, 44, 45, 48, 54, 55]
Connector = [11, 25, 35, 36, 37, 39, 52, 56, 57, 66, 67]
Special = ['NX', 'L owl', 'N owl', '5 owl', '44 owl', '48 owl', '1AX',
'1BX', '7X', '14X', '30X', '31AX', '31BX', '38AX', '38BX', 41, '76X', 60, 61, '81X','82X',
'83X', 88, '8AX', '8BX', 90, 91]

routeorder = Metro + Historic + Rapid + Frequentlocal + Grid + Connector + Special

def routeindex(n):
    if n in routeorder:
        return routeorder.index(n)
    else:
        return None

Location1 = r'N:\ServicePlanning\Signage Update\StopIDv26Database_merging.xlsx'
stops_df0 = pd.read_excel(Location1)

stops_df = stops_df0.iloc[7:,-91:]
stops_df.insert(0, 'Street ID', stops_df0.loc[:,'Street ID'])

columnlinenames = ['Line 1','Line 2','Line 3','Line 4', 'Line 5', 'Line 6', 'Line 7', 'Line 8', 'Line 9', 'Line 10', 'Line 11', 'Line 12', 'Line 13']
description = ['Line Name','Line Direction','Line Code','Line Description 1','Line Description 2', 'Line Description 3', 'Owl']

index = pd.MultiIndex.from_product([columnlinenames,description], names=['linenum', 'details'])
stop_df = stops_df.set_index('Street ID')
stop_df.columns = index
stop_df = stop_df.stack(['linenum', 'details'],dropna=False).to_frame()
stop_df.sort_index(inplace=True)

swap_df = stop_df.swaplevel(0,2)

for item in list(stop_df.index.get_level_values('Street ID')):
    for i in columnlinenames:
        stop_df.loc[item, i, 'Line Order'] = routeindex(stop_df.loc[item, i, 'Line Name'])
