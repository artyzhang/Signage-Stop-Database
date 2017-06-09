import pandas as pd
import string

Location1 = r'N:\ServicePlanning\Signage Update\TestFolder\simple_example.xlsx'

testdf = pd.read_excel(Location1)

def addone(linename):
    return linename + '1'

testdf = testdf.where((pd.notnull(testdf)),None)

simpleroutes = ['7X']

# Note to self: remember format is "testdf.loc[1,'Line 1 Name']"
# Actually start doing stuff...

itertrack = 0
for linename in testdf.loc[:,'Line 1 Name']:
    for i in simpleroutes:
        if i == linename:
            addone(testdf.loc[itertrack,'Line 1 Direction'])
    itertrack += 1

print(testdf.loc[320:330])
