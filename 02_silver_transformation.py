from pyspark.sql.functions import col, to_date

df = spark.read.format("delta").load("/mnt/adls/bronze/claims")

df_clean = df \
    .filter(col("claim_id").isNotNull()) \
    .withColumn("claim_date", to_date(col("claim_date"))) \
    .dropDuplicates()

df_clean.write.format("delta") \
    .mode("overwrite") \
    .save("/mnt/adls/silver/claims")
