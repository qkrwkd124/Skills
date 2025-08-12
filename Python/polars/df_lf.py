import time
import polars as pl

csv_path = "/appdata/storage/skils/polars/sales.csv"

#Eagar(즉시)
start = time.time()
df = pl.read_csv(csv_path)
print(f"CSV row count: {df.height}")
df = df.filter(pl.col("amount") > 100).select(["date", "amount"])
df = df.group_by("date").agg(pl.col("amount").sum())
print("Eager time:", round(time.time() - start, 3), "초")



start = time.time()
lf = (
    pl.scan_csv(csv_path)
    .filter(pl.col("amount") > 100)
    .select(["date", "amount"])
    .group_by("date")
    .agg(pl.col("amount").sum())
)
lf.collect()  # LazyFrame을 실제로 실행하여 DataFrame으로 변환
print("Lazy time:", round(time.time() - start, 3), "초")