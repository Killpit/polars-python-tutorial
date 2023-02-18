import polars as pl

#creating polars dataframe
df = pl.DataFrame(
    {
'Company': ['Ford','Toyota','Toyota','Honda','Toyota',
                    'Ford','Honda','Subaru','Ford','Subaru'],
        'Model': ['F-Series','RAV4','Camry','CR-V','Tacoma',
                  'Explorer','Accord','CrossTrek','Escape','Outback'],
        'Sales': [58283,32390,25500,18081,21837,19076,11619,15126,
                  13272,10928]
    }
)
#printing data frame
print(df)

#type of data frame
print(df.dtypes)

#columns of data frame
print(df.columns)

#rows of data frame
print(df.rows())

#selecting model
print(df.select('Model'))

#selecting model and company
print(df.select(['Model', 'Company']))

#selecting all i64 columns, RUst feature
print(df.select(pl.col(pl.Int64)))

#selecting model and sales columns and sorting by sales
print(df.select(pl.col(['Model', 'Sales'])
                .sort_by('Sales')))

#selecting multiple columns
print(df.select([pl.col(pl.Int64), 'Company']))

#getting all the string-type columns
print(df.select([pl.col(pl.Utf8)]))

#selecting rows
print(df.row(0))

#selecting multiple rows
print(df.filter(
    (pl.col('Company') == 'Toyota') | (pl.col('Company') == 'Ford')
))

#selecting rows and columns
print(df.filter(
    pl.col('Company') == 'Toyota'
).select('Model'))

#Displaying additional columns

print(df.filter(
    pl.col('Company') == 'Toyota'
).select(['Model', 'Sales']))

