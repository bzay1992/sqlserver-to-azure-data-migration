{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from pyspark.sql.functions import sum, count\
\
df = spark.read.format("delta").load("/mnt/adls/silver/claims")\
\
df_gold = df.groupBy("provider_id") \\\
    .agg(\
        count("claim_id").alias("total_claims"),\
        sum("amount").alias("total_amount")\
    )\
\
df_gold.write.format("delta") \\\
    .mode("overwrite") \\\
    .save("/mnt/adls/gold/claims_summary")}