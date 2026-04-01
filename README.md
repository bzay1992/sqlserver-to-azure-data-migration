# SQL Server to Azure Data Migration (End-to-End Data Engineering Project)\
\
## \uc0\u55357 \u56524  Overview\
This project demonstrates an enterprise-scale migration of legacy SQL Server workloads to Azure using modern data engineering practices. It showcases ETL pipeline design, data transformation, validation, and cloud-native architecture.\
\
## \uc0\u55357 \u56960  Architecture\
- Source: SQL Server (on-prem simulation)\
- Ingestion: Azure Data Factory\
- Storage: Azure Data Lake Gen2 (Bronze/Silver/Gold)\
- Processing: Azure Databricks (PySpark)\
- Warehouse: Azure Synapse Analytics\
- CI/CD: Azure DevOps\
\
## \uc0\u55356 \u57303 \u65039  Data Flow\
1. Extract data from SQL Server using ADF\
2. Load raw data into ADLS (Bronze)\
3. Transform data using Databricks (Silver)\
4. Aggregate into business-ready format (Gold)\
5. Load into Synapse for analytics\
\
## \uc0\u55358 \u56816  Tech Stack\
- Azure Data Factory\
- Azure Databricks (PySpark)\
- Azure Synapse\
- ADLS Gen2\
- SQL Server\
- Python / SQL\
\
## \uc0\u55357 \u56580  Key Features\
- Incremental data loading (watermark-based)\
- Medallion Architecture (Bronze\'96Silver\'96Gold)\
- Data validation and quality checks\
- CI/CD pipeline integration\
\
## \uc0\u55357 \u56522  Results\
- Reduced processing latency by ~50%\
- Improved scalability and performance\
- Automated data pipelines with minimal manual intervention\
\
## \uc0\u9888 \u65039  Challenges & Solutions\
- **Schema mismatch** \uc0\u8594  Implemented schema enforcement in PySpark  \
- **Slow queries** \uc0\u8594  Optimized indexing in SQL Server  \
- **Data consistency** \uc0\u8594  Built validation framework  \
\
## \uc0\u55357 \u56513  Project Structure\
(Refer to repo folders)\
\
## \uc0\u55357 \u56424 \u8205 \u55357 \u56507  Author\
Bijay Devkota}
