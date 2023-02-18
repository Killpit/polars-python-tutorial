import polars as pl
import time

#implicit lazy method, uses lazy evaluation, uses filter() to optimize
start = time.time()
df = pl.scan_csv("/Users/atatekeli/PycharmProjects/PolarsTutorial/flights.csv").filter(
        (pl.col('MONTH') == 12) &
        (pl.col('ORIGIN_AIRPORT') == 'SEA') &
        (pl.col('DESTINATION_AIRPORT') == 'DFW')).collect()
end = time.time()
print(end - start)
print(df)