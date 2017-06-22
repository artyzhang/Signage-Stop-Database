import pandas as pd

Location1 = r'N:\ServicePlanning\Signage Update\TestFolder\StopDatabase_forcleaning.xlsx'
stops_df = pd.read_excel(Location1)

columnlinenames = ['Line 1','Line 2','Line 3','Line 4', 'Line 5', 'Line 6', 'Line 7', 'Line 8', 'Line 9', 'Line 10', 'Line 11', 'Line 12', 'Line 13']
columndirectionnames = ['Line 1 Direction','Line 2 Direction','Line 3 Direction','Line 4 Direction', 'Line 5 Direction', 'Line 6 Direction',
 'Line 7 Direction', 'Line 8 Direction', 'Line 9 Direction', 'Line 10 Direction', 'Line 11 Direction', 'Line 12 Direction', 'Line 13 Direction']
columnnames = ['Line 1','Line 1 Direction','Line 2','Line 2 Direction','Line 3','Line 3 Direction','Line 4','Line 4 Direction',
'Line 5','Line 5 Direction','Line 6', 'Line 6 Direction','Line 7','Line 7 Direction', 'Line 8', 'Line 8 Direction',
'Line 9', 'Line 9 Direction','Line 10', 'Line 10 Direction','Line 11', 'Line 11 Direction', 'Line 12', 'Line 12 Direction', 'Line 13', 'Line 13 Direction']

acceptablelines = ['1', '10' ,'12', '14','14R','14X','18','19','1AX','1BX',
'2','21','22','23','24','25','27','28','28R','29',
'3','30','30X','31','31AX','31BX','33','35','36','37','38','38AX','38BX','38R','39',
'41','43','44','44 owl','45','47','48','48 owl','49',
'5','5R','5 owl','52','54','55','56','57','59',
'6','60','61','66','67',
'7','76X','7X',
'8','81X','82X','83X','88','8AX','8BX',
'9','9R','90','91',
'E','F','J','K','L','L owl','M','N','N owl','NX','T']

allroutes =[]
for name in columnlinenames:
    for value in stops_df.loc[:,name]:
        allroutes.append(value)
allroutes = set(allroutes)
print(allroutes)

alluniqueroutes = pd.Series(sorted(list(allroutes), key=lambda x: str(x)))
Locationfinal = r'N:\ServicePlanning\Signage Update\TestFolder\StopIDV26_alluniqueroutes.xlsx'
alluniqueroutes.to_excel(Locationfinal, sheet_name = 'Sheet1', engine = 'xlsxwriter', index = False)
