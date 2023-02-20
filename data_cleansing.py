import polars as pl

#data cleansing and null values is_null(), sum()=sum
#any()=columns that contain null
#all()=columns are null
q = (
    pl.scan_csv('/Users/atatekeli/PycharmProjects/PolarsTutorial/titanic_train.csv')
    #.select(pl.col('Cabin').is_null().all())
)

#Iterating for null values
for col in q.collect(): print(f'{col.name} - {col.is_null().sum()}')


#df = q.collect()
#print(df)