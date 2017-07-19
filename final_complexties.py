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

Location1 = r"N:\ServicePlanning\Signage Update\Signage-Stop-Database-master\StopIDv26Database_sorted.xlsx"
Location2 = r'N:\ServicePlanning\Signage Update\TestFolder\stop_categorization.xlsx'
stops_df = pd.read_excel(Location1)
reference_df = pd.read_excel(Location2)

columnlinenames = ['Line 1','Line 2','Line 3','Line 4', 'Line 5', 'Line 6', 'Line 7', 'Line 8', 'Line 9', 'Line 10']

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
for ind in range(len(stops_df)):
    for name in columnlinenames:
        if pd.isnull(stops_df.loc[ind, columnplus2(stops_df, name)]):
            if tryint(stops_df.loc[ind,name]) in reference_list:
                lookup = tryint(stops_df.loc[ind,name])
                if stops_df.loc[ind,"Stop ID"] in reference_dict[lookup].keys():
                    if reference_dict[lookup][stops_df.loc[ind,"Stop ID"]] != '<Null>':
                        stops_df.loc[ind, columnplus2(stops_df, name)] = reference_dict[lookup][stops_df.loc[ind,"Stop ID"]]
                        #print('Match for '  + str(lookup) + ' and ' + str(stops_df.loc[ind,"Stop ID"]))
                    else:
                        troubleshooting.append(['Null',stops_df.loc[ind,name],stops_df.loc[ind,"Stop ID"]])
                else:
                    troubleshooting.append(['No match',stops_df.loc[ind,name],stops_df.loc[ind,"Stop ID"]])

troubleshoot_df = pd.DataFrame.from_records(troubleshooting, columns = ['Type of error','Line','Stop ID'])
troubleshoot_df.to_excel(r"N:\ServicePlanning\Signage Update\TestFolder\conflicts.xlsx")

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
                       'Line 10','Line 10 Route',]].to_excel(Location3)
