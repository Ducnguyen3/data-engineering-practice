import os
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.window import Window

# Đảm bảo Spark nhận đúng Python khi chạy Docker hoặc Windows
os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"

def load_data(spark, path):
    return spark.read.option("header", True).option("inferSchema", True).csv(path)

def add_source_file(df):
    return df.withColumn("source_file", F.input_file_name())

def extract_file_date(df):
    return df.withColumn(
        "file_date",
        F.to_date(F.regexp_extract("source_file", r"(\d{4}-\d{2}-\d{2})", 1))
    )

def add_brand(df):
    return df.withColumn(
        "brand",
        F.when(F.col("model").contains(" "), F.split("model", " ").getItem(0)).otherwise("unknown")
    )

def add_storage_ranking(df):
    ranking_df = df.select("model", "capacity_bytes").distinct()
    window = Window.orderBy(F.col("capacity_bytes").desc())
    ranking_df = ranking_df.withColumn("storage_ranking", F.dense_rank().over(window))
    return df.join(ranking_df, on=["model", "capacity_bytes"], how="left")

def add_primary_key(df):
    return df.withColumn("primary_key", F.hash("date", "serial_number", "model"))

def main():
    spark = SparkSession.builder.appName("Exercise7").getOrCreate()

    path = "data/hard-drive-2022-01-01-failures.csv"
    df = load_data(spark, path)
    df = add_source_file(df)
    df = extract_file_date(df)
    df = add_brand(df)
    df = add_storage_ranking(df)
    df = add_primary_key(df)

    df.select("serial_number", "model", "capacity_bytes", "source_file", "file_date", "brand", "storage_ranking", "primary_key") \
      .show(20, truncate=False)

    spark.stop()

if __name__ == "__main__":
    main()
