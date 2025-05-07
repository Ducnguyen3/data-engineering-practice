from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, col, to_date, desc, row_number, max, expr, year
from pyspark.sql.window import Window
import zipfile
import os

def unzip_csv_files(input_folder="data", output_folder="unzipped_data"):
    os.makedirs(output_folder, exist_ok=True)
    for file in os.listdir(input_folder):
        if file.endswith(".zip"):
            with zipfile.ZipFile(os.path.join(input_folder, file), 'r') as zip_ref:
                zip_ref.extractall(output_folder)

def read_data(spark, path):
    return spark.read.option("header", True).csv(path, inferSchema=True)

def average_trip_duration_per_day(df):
    df.groupBy(to_date("start_time").alias("date")) \
      .agg(avg("tripduration").alias("avg_duration")) \
      .write.mode("overwrite").option("header", True).csv("reports/avg_duration_per_day")

def trips_count_per_day(df):
    df.groupBy(to_date("start_time").alias("date")) \
      .agg(count("*").alias("trip_count")) \
      .write.mode("overwrite").option("header", True).csv("reports/trip_count_per_day")

def most_popular_start_station_per_month(df):
    df = df.withColumn("month", expr("substring(start_time, 0, 7)"))
    window = Window.partitionBy("month").orderBy(desc("count"))
    df.groupBy("month", "from_station_name") \
      .count() \
      .withColumn("rank", row_number().over(window)) \
      .filter(col("rank") == 1) \
      .drop("rank") \
      .write.mode("overwrite").option("header", True).csv("reports/popular_start_per_month")

def average_duration_by_gender(df):
    df.groupBy("gender") \
      .agg(avg("tripduration").alias("avg_duration")) \
      .write.mode("overwrite").option("header", True).csv("reports/avg_duration_by_gender")

def top_10_ages_longest_shortest(df):
    df = df.withColumn("age", 2025 - col("birthyear"))
    df.filter(col("age").isNotNull()) \
      .orderBy(desc("tripduration")) \
      .select("age", "tripduration") \
      .limit(10) \
      .write.mode("overwrite").option("header", True).csv("reports/top10_longest_trips")
    
    df.filter(col("age").isNotNull()) \
      .orderBy("tripduration") \
      .select("age", "tripduration") \
      .limit(10) \
      .write.mode("overwrite").option("header", True).csv("reports/top10_shortest_trips")

def main():
    spark = SparkSession.builder.appName("Exercise6").getOrCreate()

    # Step 1: unzip files to folder
    unzip_csv_files()

    # Step 2: Read all csvs from the unzipped folder
    df = read_data(spark, "unzipped_data/*.csv")
    df = df.withColumn("tripduration", col("tripduration").cast("double"))

    # Step 3: Make sure reports/ exists
    os.makedirs("reports", exist_ok=True)

    # Step 4: Run analytics
    average_trip_duration_per_day(df)
    trips_count_per_day(df)
    most_popular_start_station_per_month(df)
    average_duration_by_gender(df)
    top_10_ages_longest_shortest(df)

    spark.stop()

if __name__ == "__main__":
    main()