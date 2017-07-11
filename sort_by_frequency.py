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

def columnplus1(df, dfcolumn1):
    return df.columns.values[df.columns.get_loc(dfcolumn1)+1]

def columnplus2(df, dfcolumn1):
    return df.columns.values[df.columns.get_loc(dfcolumn1)+2]

def columnplus3(df, dfcolumn1):
    return df.columns.values[df.columns.get_loc(dfcolumn1)+3]

def columnplus4(df, dfcolumn1):
    return df.columns.values[df.columns.get_loc(dfcolumn1)+4]

def columnplus5(df, dfcolumn1):
    return df.columns.values[df.columns.get_loc(dfcolumn1)+5]

def columnplus6(df, dfcolumn1):
    return df.columns.values[df.columns.get_loc(dfcolumn1)+6]

def tryint(v):
    try:
        return int(v)
    except ValueError:
        return v


columnlinenames = ['Line 1','Line 2','Line 3','Line 4', 'Line 5', 'Line 6', 'Line 7', 'Line 8', 'Line 9', 'Line 10', 'Line 11', 'Line 12', 'Line 13']

Location1 = r'N:\ServicePlanning\Signage Update\StopIDv26Database_merging.xlsx'
stops_df = pd.read_excel(Location1)

def sortbyroutelist(df, i, columnlist):
    return [routeindex(tryint(x)) for x in [df.loc[i,j] for j in columnlist]]


def stopdfplus(ind, dfc, num):
    # This relies on the stops_df dataframe
    if num == 1:
        return stops_df.loc[ind,columnplus1(stops_df,dfc)]
    elif num == 2:
        return stops_df.loc[ind,columnplus2(stops_df,dfc)]
    elif num == 3:
        return stops_df.loc[ind,columnplus3(stops_df,dfc)]
    elif num == 4:
        return stops_df.loc[ind,columnplus4(stops_df,dfc)]
    elif num == 5:
        return stops_df.loc[ind,columnplus5(stops_df,dfc)]
    elif num == 6:
        return stops_df.loc[ind,columnplus6(stops_df,dfc)]

def generateentry(num, columnlist):
    # This relies on the stops_df dataframe
    longlist = []
    for b in columnlist:
        longlist.append([stops_df.loc[num, b],stopdfplus(num,b,1),stopdfplus(num,b,2),stopdfplus(num,b,3),
                     stopdfplus(num,b,4),stopdfplus(num,b,5),stopdfplus(num,b,6)])
    return longlist

def generateentrylist(i):
    # This relies on the stops_df dataframe and the columnlinenames list
    return [x for (y,x) in sorted(zip(sortbyroutelist(stops_df, i, columnlinenames),generateentry(i,columnlinenames)), key=lambda x: x[0] if x[0] else np.inf)]

staging_dict = {}
for a in range(7, len(stops_df)):
    staging_dict[a] = [i for sublist in generateentrylist(a) for i in sublist]

staging_stopsdf = pd.DataFrame.from_dict(staging_dict, orient = 'index')
Location2 = r"N:\ServicePlanning\Signage Update\TestFolder\organized_staging.xlsx"
staging_stopsdf.to_excel(Location2)
