import time
import polars as pl

csv_path = "/appdata/storage/skils/polars/sales.csv"

#Eagar(즉시)
start = time.time()
df = pl.read_csv(csv_path)
print(df.head())
df = df.filter(pl.col("amount") > 100).select(["date", "amount"])
print(df.head())
df = df.group_by("date").agg(pl.col("amount").sum())
print(df.head())
print("Eager time:", round(time.time() - start, 3), "초")



