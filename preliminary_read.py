import pandas as pd

Location1 = r'N:\ServicePlanning\Signage Update\Signage-Stop-Database-master\StopIDV25_Trpz_merging_database.xlsx'
stops_df = pd.read_excel(Location1)

# "Lines Served By Stops" = Column 19
<<<<<<< HEAD
# "line 1 Name" = Column 25

print(stops_df.iloc[:5,[19] + list(range(25,37))])
=======
# Lines and Directions = Column 25-37
#print(stops_df.iloc[:5,[19] + list(range(25,37))])

linelist_dict = {}

inex = 0
for com in stops_df.loc[:, 'Lines Served by Direction']:
    linelist_dict[inex] = list(map(lambda x: x.strip(), com.split(',') )) if ',' in com else [com.strip()]
    inex += 1

lines_list_df = pd.DataFrame.from_dict(linelist_dict, orient = 'index')

print(lines_list_df.head())
>>>>>>> origin/master
