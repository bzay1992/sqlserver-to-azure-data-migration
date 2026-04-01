{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from pyspark.sql.functions import col, to_date\
\
df = spark.read.format("delta").load("/mnt/adls/bronze/claims")\
\
df_clean = df \\\
    .filter(col("claim_id").isNotNull()) \\\
    .withColumn("claim_date", to_date(col("claim_date"))) \\\
    .dropDuplicates()\
\
df_clean.write.format("delta") \\\
    .mode("overwrite") \\\
    .save("/mnt/adls/silver/claims")}