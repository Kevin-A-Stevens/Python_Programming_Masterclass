"""
Pandas can read and output various forms of data
pip3 install sqlalchemy
pip3 install lxml
pip3 install html5lib
pip3 install BeautifulSoup4
pip3 install xlrd
"""
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('example')
print(df)

print()

df.to_csv('my_output', index=False)
print(pd.read_csv('my_output'))

print()
# my_excel = pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1')
# print(my_excel)
# df.to_excel('Excel_Sample2.xlsx', sheet_name='NewSheet')

# HTML
data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')

# https://www.fdic.gov/bank/individual/failed/banklist.html

print(data[0].head())

# SQL
engine = create_engine('sqlite:///:memory:')
df.to_sql('my_table', engine)

sqldf = pd.read_sql('my_table', con=engine)
print(sqldf)
