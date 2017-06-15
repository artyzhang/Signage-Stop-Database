import pandas as pd

Location1 = r'N:\ServicePlanning\Signage Update\TestFolder\StopDatabase_forcleaning.xlsx'
stops_df = pd.read_excel(Location1)

columnlinenames = ['Line 1','Line 2','Line 3','Line 4', 'Line 5', 'Line 6', 'Line 7', 'Line 8', 'Line 9', 'Line 10', 'Line 11', 'Line 12', 'Line 13']
columndirectionnames = ['Line 1 Direction','Line 2 Direction','Line 3 Direction','Line 4 Direction', 'Line 5 Direction', 'Line 6 Direction',
 'Line 7 Direction', 'Line 8 Direction', 'Line 9 Direction', 'Line 10 Direction', 'Line 11 Direction', 'Line 12 Direction', 'Line 13 Direction']
columnnames = ['Line 1','Line 1 Direction','Line 2','Line 2 Direction','Line 3','Line 3 Direction','Line 4','Line 4 Direction',
'Line 5','Line 5 Direction','Line 6', 'Line 6 Direction','Line 7','Line 7 Direction', 'Line 8', 'Line 8 Direction',
'Line 9', 'Line 9 Direction','Line 10', 'Line 10 Direction','Line 11', 'Line 11 Direction', 'Line 12', 'Line 12 Direction', 'Line 13', 'Line 13 Direction']

allroutes =[]
for name in columnlinenames:
    for value in stops_df.loc[:,name]:
        allroutes.append(value)
allroutes = set(allroutes)
print(allroutes)

alluniqueroutes = pd.Series(sorted(list(allroutes), key=lambda x: str(x)))
Locationfinal = r'N:\ServicePlanning\Signage Update\TestFolder\StopIDV26_alluniqueroutes.xlsx'
alluniqueroutes.to_excel(Locationfinal, sheet_name = 'Sheet1', engine = 'xlsxwriter', index = False)
