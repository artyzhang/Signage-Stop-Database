import pandas as pd
import numpy as np

Location1 = r'N:\ServicePlanning\Signage Update\StopIDv26Database_merging.xlsx'
stops_df0 = pd.read_excel(Location1)

stops_df = stops_df0.iloc[7:,-91:]
stops_df.insert(0, 'Street ID', stops_df0.loc[:,'Street ID'])

columnlinenames = ['Line 1','Line 2','Line 3','Line 4', 'Line 5', 'Line 6', 'Line 7', 'Line 8', 'Line 9', 'Line 10', 'Line 11', 'Line 12', 'Line 13']
description = ['Line Name','Line Direction','Line Code','Line Description 1','Line Description 2', 'Line Description 3', 'Owl']

index = pd.MultiIndex.from_product([columnlinenames,description], names=['linenum', 'details'])
stops_df = stops_df.set_index('Street ID')
stops_df.columns = index
stops_ser = stops_df.stack(['linenum', 'details'],dropna=False)
