from pyspark.sql.functions import sum, count

df = spark.read.format("delta").load("/mnt/adls/silver/claims")

df_gold = df.groupBy("provider_id") \
    .agg(
        count("claim_id").alias("total_claims"),
        sum("amount").alias("total_amount")
    )

df_gold.write.format("delta") \
    .mode("overwrite") \
    .save("/mnt/adls/gold/claims_summary")
