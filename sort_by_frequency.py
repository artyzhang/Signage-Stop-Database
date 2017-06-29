import pandas as pd

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

columnlinenames = ['Line 1 Name','Line 2 Name','Line 3 Name','Line 4 Name', 'Line 5 Name', 'Line 6 Name', 'Line 7 Name', 'Line 8 Name',
'Line 9 Name', 'Line 10 Name', 'Line 11 Name', 'Line 12 Name', 'Line 13 Name']

Location1 = r'C:\Temp_CS\Signage-Stop-Database\StopDatabase_RoutesOnly.xlsx'
stops_df = pd.read_excel(Location1)
stops_dict = {}

for l in range(len(stops_df)):
    routelist = []
    for m in columnlinenames:
        routelist.append(stops_df.loc[l,m])
    stops_dict[l] = routelist

for l in range(5):
    print(stops_dict[l])
