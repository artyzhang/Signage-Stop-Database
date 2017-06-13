import pandas as pd

Location1 = r'N:\ServicePlanning\Signage Update\Signage-Stop-Database-master\StopDatabase_RoutesOnly.xlsx'
stops_df = pd.read_excel(Location1)

#

print(stops_df.head())
