import pandas as pd
import string

Location1 = r'N:\ServicePlanning\Signage Update\Signage-Stop-Database-master\StopDatabase_RoutesOnly.xlsx'

stops_df = pd.read_excel(Location1)

stops_df = stops_df.where((pd.notnull(stops_df)),None)

simpleroutes = ['1', '1AX','1BX','2', '3', '5R', '6', '7','7X', '8', '9R', '11', '12', '14', '14R', '14X', '18', '19', '21', '23',
'25', '27', '28R','30X','31','31AX','31BX','35', '38AX','38BX','38R','39', '41','47', '49', '52', '54', '55', '56', '66', '67', '76X', '82X',
'83X', '88','J','K','L','NX','T']

one_direction_simple_only = ['8AX', '8BX', '37', '45', '81X', 'N']
one_direction_simple_direction = {'8AX': 'OB','8BX': 'OB', '37': 'OB', '45':'OB', 'N':'OB'}

owl_simple_only = ['44 owl', '48 owl', 'L owl', 'N owl']

# Note to self: remember format is "testdf.loc[1,'Line 1 Name']"
# find and replace

def addone(linename):
    return linename + '1'

def followingcolumn(df, dfcolumn1):
    return df.columns.values[df.columns.get_loc(dfcolumn1)+1]

def columnafternext(df, dfcolumn1):
    return df.columns.values[df.columns.get_loc(dfcolumn1)+2]

# Actually start doing stuff...

Columnnumbers = ['Line 1 Name','Line 2 Name','Line 3 Name','Line 4 Name','Line 5 Name','Line 6 Name','Line 7 Name','Line 8 Name','Line 9 Name',
'Line 10 Name','Line 11 Name','Line 12 Name','Line 13 Name']

for k in Columnnumbers:
    co = stops_df.columns.get_loc(k) + 2
    stops_df.insert(co, k[:-5] + ' Route' , stops_df[k].where(stops_df[k].isin(simpleroutes), None))

for j in Columnnumbers:
    for ln in range(len(stops_df)):
        if str(stops_df.loc[ln,j]) in simpleroutes:
            stops_df.loc[ln, followingcolumn(stops_df,j)] = str(stops_df.loc[ln, followingcolumn(stops_df,j)]) + '1'
            stops_df.loc[ln, columnafternext(stops_df,j)] = str(stops_df.loc[ln,j]) + str(stops_df.loc[ln,followingcolumn(stops_df,j)])

#for m in Columnnumbers:
#    for mn in range(len(stops_df)):
#        if str(stops_df.loc[mn,m]) in one_direction_simple_only:
#            if stops_df.loc[mn, followingcolumn(stops_df,m)] == one_direction_simple_direction[stops_df.loc[mn,m]]
#               stops_df.loc[mn, followingcolumn(stops_df,m)] = str(stops_df.loc[mn, followingcolumn(stops_df,m)]) + '1'
#               stops_df.loc[mn, columnafternext(stops_df,m)] = str(stops_df.loc[mn,m]) + str(stops_df.loc[ln,followingcolumn(stops_df,m)])

Locationfinal = r'N:\ServicePlanning\Signage Update\TestFolder\StopDatabase_SimpleRoutesjoined.xlsx'
stops_df.to_excel(Locationfinal, sheet_name = 'Sheet1', engine = 'xlsxwriter', index = False)
