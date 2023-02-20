import polars as pl

q = (
    pl.scan_csv('/Users/atatekeli/PycharmProjects/PolarsTutorial/titanic_train.csv')
    .select(
        [
            #pl.exclude('Cabin'),
            #Set all columns except Cabin
            #pl.col('Cabin').fill_null(strategy='backward')

            pl.exclude('Age'),
            pl.col('Age').fill_null(value=0)
        ]
    )
)

print(q)