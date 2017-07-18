import pandas as pd

def columnplus2(df, dfcolumn1):
    return df.columns.values[df.columns.get_loc(dfcolumn1)+2]

def tryint(v):
    try:
        return int(v)
    except ValueError:
        return v

def trystr(v):
     try:
         dummy = int(v)
     except ValueError:
         return True
     return False

Location1 = r'N:\ServicePlanning\Signage Update\StopIDv26Database_merging.xlsx'
Location2 = r'N:\ServicePlanning\Signage Update\TestFolder\stop_categorization.xlsx'
stops_df = pd.read_excel(Location1)
reference_df = pd.read_excel(Location2)

columnlinenames = ['Line 1','Line 2','Line 3','Line 4', 'Line 5', 'Line 6', 'Line 7', 'Line 8', 'Line 9', 'Line 10', 'Line 11', 'Line 12', 'Line 13']

# Create a nested dictionary object where the keys are a route number, paired to another dictionary
# in which the stop ID's are keys that are paired to the appropriate code
reference_list_len4 = list(set(reference_df['ROUTE_NAME'].tolist()))
reference_list = [x.strip() if trystr(x) else x for x in reference_list_len4]
reference_dict = {}
for d in reference_list:
    nested_ref = {}
    for j in range(len(reference_df)):
        if reference_df.loc[j,'ROUTE_NAME'] == reference_list_len4[reference_list.index(d)]:
            nested_ref[reference_df.loc[j, 'STOPID']] = reference_df.loc[j,'category']
    reference_dict[d] = nested_ref

troubleshooting = []
for ind in range(7,len(stops_df)):
    for name in columnlinenames:
        if tryint(stops_df.loc[ind,name]) in reference_list:
            lookup = tryint(stops_df.loc[ind,name])
            if stops_df.loc[ind,"Stop ID"] in reference_dict[lookup].keys():
                if reference_dict[lookup][stops_df.loc[ind,"Stop ID"]] != '<Null>':
                    stops_df.loc[ind, columnplus2(stops_df, name)] = reference_dict[lookup][stops_df.loc[ind,"Stop ID"]]
                    #print('Match for '  + str(lookup) + ' and ' + str(stops_df.loc[ind,"Stop ID"]))
                else:
                    stops_df.loc[ind, columnplus2(stops_df, name)] = 'NULL'
                    troubleshooting.append(['Null',stops_df.loc[ind,name],stops_df.loc[ind,"Stop ID"]])
            else:
                stops_df.loc[ind, columnplus2(stops_df, name)] = 'No Match'
                troubleshooting.append(['No match',stops_df.loc[ind,name],stops_df.loc[ind,"Stop ID"]])

print(troubleshooting)
Location3 = r"N:\ServicePlanning\Signage Update\TestFolder\test_final_ties.xlsx"
stops_df.loc[:,['Stop ID','Line 1','Line 1 Route',
                       'Line 2','Line 2 Route',
                       'Line 3','Line 3 Route',
                       'Line 4','Line 4 Route',
                       'Line 5','Line 5 Route',
                       'Line 6','Line 6 Route',
                       'Line 7','Line 7 Route',
                       'Line 8','Line 8 Route',
                       'Line 9','Line 9 Route',
                       'Line 10','Line 10 Route',
                       'Line 11','Line 11 Route',
                       'Line 12','Line 12 Route'
                       'Line 13','Line 13 Route']].to_excel(Location3)
