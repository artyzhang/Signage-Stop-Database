import pandas as pd

Location1 = r'N:\ServicePlanning\Signage Update\Signage-Stop-Database-master\StopIDV26_Trpz_merging.xlsx'
stops_df = pd.read_excel(Location1)

def splitcomma(strin):
    return list(map(lambda x: x.strip(), strin.split(','))) if ',' in strin else [strin.strip()]

def splitdashIBOB(strin):
    if '-' in strin:
        twoitems = strin.split('-')
        if len(twoitems) == 2 and twoitems[1] == 'IB' or twoitems[1] == 'OB':
            return twoitems
        else:
            return [strin,'FLAG']
    else:
        return [strin,'FLAG']

def split(strin):
    fulllist = []
    for stritem in splitcomma(strin):
        fulllist.extend(splitdashIBOB(stritem))
    return fulllist

###

linelist_dict = {}
inex = 0
for com in stops_df.loc[:, 'Lines Served by Direction']:
    linelist_dict[inex] = split(com)
    inex += 1

lines_list_df = pd.DataFrame.from_dict(linelist_dict, orient = 'index')
columnlinenames = ['Line 1','Line 2','Line 3','Line 4', 'Line 5', 'Line 6', 'Line 7', 'Line 8', 'Line 9', 'Line 10', 'Line 11', 'Line 12', 'Line 13']
columndirectionnames = ['Line 1 Direction','Line 2 Direction','Line 3 Direction','Line 4 Direction', 'Line 5 Direction', 'Line 6 Direction',
 'Line 7 Direction', 'Line 8 Direction', 'Line 9 Direction', 'Line 10 Direction', 'Line 11 Direction', 'Line 12 Direction', 'Line 13 Direction']
columnnames = ['Line 1','Line 1 Direction','Line 2','Line 2 Direction','Line 3','Line 3 Direction','Line 4','Line 4 Direction',
'Line 5','Line 5 Direction','Line 6', 'Line 6 Direction','Line 7','Line 7 Direction', 'Line 8', 'Line 8 Direction',
'Line 9', 'Line 9 Direction','Line 10', 'Line 10 Direction','Line 11', 'Line 11 Direction', 'Line 12', 'Line 12 Direction', 'Line 13', 'Line 13 Direction']

nameinex = 0
for name in columnnames:
    stops_df[name] = lines_list_df[nameinex]
    nameinex += 1

Locationfinal = r'N:\ServicePlanning\Signage Update\TestFolder\StopIDV26StopDatabase_forcleaning.xlsx'
stops_df.to_excel(Locationfinal, sheet_name = 'Sheet1', engine = 'xlsxwriter', index = False)

# new columns are range(20,46)
