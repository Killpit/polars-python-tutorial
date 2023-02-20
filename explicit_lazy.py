import polars as pl
import time

start = time.time()
df = pl.read_csv('/Users/atatekeli/PycharmProjects/PolarsTutorial/flights.csv').lazy().filter(
        (pl.col('MONTH') == 12) &
        (pl.col('ORIGIN_AIRPORT') == 'SEA') &
        (pl.col('DESTINATION_AIRPORT') == 'DFW')).collect()
end = time.time()

print(end - start)
print(df)

