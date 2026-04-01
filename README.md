# SQL Server to Azure Data Migration (End-to-End Data Engineering Project)

## 📌 Overview
This project demonstrates an enterprise-scale migration of legacy SQL Server workloads to Azure using modern data engineering practices. It showcases ETL pipeline design, data transformation, validation, and cloud-native architecture.

## 🚀 Architecture
- Source: SQL Server (on-prem simulation)
- Ingestion: Azure Data Factory
- Storage: Azure Data Lake Gen2 (Bronze/Silver/Gold)
- Processing: Azure Databricks (PySpark)
- Warehouse: Azure Synapse Analytics
- CI/CD: Azure DevOps

## 🏗️ Data Flow
1. Extract data from SQL Server using ADF
2. Load raw data into ADLS (Bronze)
3. Transform data using Databricks (Silver)
4. Aggregate into business-ready format (Gold)
5. Load into Synapse for analytics

## 🧰 Tech Stack
- Azure Data Factory
- Azure Databricks (PySpark)
- Azure Synapse
- ADLS Gen2
- SQL Server
- Python / SQL

## 🔄 Key Features
- Incremental data loading (watermark-based)
- Medallion Architecture (Bronze–Silver–Gold)
- Data validation and quality checks
- CI/CD pipeline integration

## 📊 Results
- Reduced processing latency by ~50%
- Improved scalability and performance
- Automated data pipelines with minimal manual intervention

## ⚠️ Challenges & Solutions
- **Schema mismatch** → Implemented schema enforcement in PySpark  
- **Slow queries** → Optimized indexing in SQL Server  
- **Data consistency** → Built validation framework  

## 📁 Project Structure
(Refer to repo folders)

## 👨‍💻 Author
Bijay Devkota
