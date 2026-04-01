from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BronzeIngestion").getOrCreate()

df = spark.read.format("csv") \
    .option("header", "true") \
    .load("/mnt/adls/bronze/claims_raw.csv")

df.write.format("delta") \
    .mode("overwrite") \
    .save("/mnt/adls/bronze/claims")
