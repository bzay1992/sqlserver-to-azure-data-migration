df = spark.read.format("delta").load("/mnt/adls/silver/claims")

null_count = df.filter("claim_id IS NULL").count()

if null_count > 0:
    raise Exception("Data Quality Check Failed: Null claim_id found")

print("Data validation passed")
