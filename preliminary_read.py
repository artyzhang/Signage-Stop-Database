import pandas as pd

Location1 = r'N:\ServicePlanning\Signage Update\Signage-Stop-Database-master\StopIDV25_Trpz_merging_database.xlsx'
stops_df = pd.read_excel(Location1)

# "Lines Served By Stops" = Column 19
# "line 1 Name" = Column 25

print(stops_df.iloc[:5,[19] + list(range(25,37))])
