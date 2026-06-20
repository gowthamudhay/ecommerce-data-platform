# E-Commerce Data Platform (End-to-End AWS Data Engineering Project)

## Overview
This project demonstrates a complete end-to-end data pipeline that simulates a real-world e-commerce analytics system. It covers data ingestion, transformation, storage, querying, and visualization.

The goal is to convert raw e-commerce data into meaningful business insights using modern data engineering tools.

---

## Architecture

Raw Data (CSV)
   ↓
Amazon S3 (Raw Layer)
   ↓
AWS Glue (ETL Processing)
   ↓
Amazon S3 (Processed Parquet Layer)
   ↓
Amazon Athena (SQL Querying)
   ↓
Power BI (Dashboard & Visualization)

---

## Tech Stack

- Amazon S3 – Data storage (raw & processed layers)
- AWS Glue – ETL data transformation using PySpark
- Amazon Athena – Serverless SQL queries on S3 data
- Power BI – Data visualization and dashboard creation
- Python (PySpark) – Data processing and cleaning

---

## Dataset Description

The project simulates an e-commerce environment with the following datasets:

- Customers: Customer information such as ID and country
- Products: Product catalog with categories and pricing
- Reviews: Customer feedback and ratings

---

## Data Engineering Process

### 1. Data Ingestion
Raw CSV files are uploaded into Amazon S3 (raw layer).

### 2. Data Transformation (ETL)
AWS Glue jobs are used to:
- Remove null values
- Remove duplicates
- Standardize data types
- Filter invalid records

### 3. Data Storage (Processed Layer)
Cleaned data is stored in Parquet format in S3 for optimized querying.

### 4. Data Querying
Amazon Athena is used to run SQL queries directly on processed S3 data.

### 5. Data Visualization
Power BI is used to build dashboards for business insights.

---

## Key Insights

- Total number of customers analyzed
- Customer distribution by country
- Product category distribution
- Product catalog overview

---

## Key Skills Demonstrated

- Data pipeline design
- ETL development using AWS Glue
- Data lake architecture using S3
- Serverless querying using Athena
- Data visualization using Power BI
- Working with structured and semi-structured data

---

## Project Structure
