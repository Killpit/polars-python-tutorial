import polars as pl
import time

start = time.time()

data = pl.read_csv("/Users/atatekeli/PycharmProjects/PolarsTutorial/flights.csv").filter(
    (pl.col('MONTH') == 12) &
    (pl.col('ORIGIN_AIRPORT') == 'SEA') &
    (pl.col('DESTINATION_AIRPORT') =='DFW'))
end = time.time()

print(end - start)
print(data)
