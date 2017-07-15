import pandas as pd

def columnplus2(df, dfcolumn1):
    return df.columns.values[df.columns.get_loc(dfcolumn1)+2]

def tryint(v):
    try:
        return int(v)
    except ValueError:
        return v

Location1 = r'N:\ServicePlanning\Signage Update\StopIDv26Database_merging.xlsx'
Location2 = r''
stops_df = pd.read_excel(Location1)
reference_df = pd.read_excel(Location2)

columnlinenames = ['Line 1','Line 2','Line 3','Line 4', 'Line 5', 'Line 6', 'Line 7', 'Line 8', 'Line 9', 'Line 10', 'Line 11', 'Line 12', 'Line 13']

# Create a nested dictionary object where the keys are a route number, paired to another dictionary
# in which the stop ID's are keys that are paired to the appropriate code
reference_list = set(reference_dict['route'].tolist)
reference_dict = {}
for d in reference_list:
    nested_ref = {}
    for j in range(len(reference_df)):
        nested_ref[reference_df.loc[j, 'Stop ID']] = reference_dict.loc[j,'category']
    reference_dict[d] = nested_ref

for ind in range(7,len(stops_df)):
    for name in columnlinenames:
        if stops_df.loc[ind,name] in reference_list:
            lookup = stops_df.loc[ind,name]
            if reference_dict[lookup][stops_df.loc[ind,"StopID"]]:
                stops_df.loc[ind, columnplus2(stops_df, name)] = reference_dict[lookup][stops_df.loc[ind,"StopID"]]
            else:
                stops_df.loc[ind, "specific Line Code"] = 'No Match'

Location3 =
stops_df.to_excel(Location3)
