# Dat Architecture

## Overview

Key benefits of a data warehouse considered in this proposal:

* Informed decision making
* Consolidated data from many sources
* Historical data analysis
* Data quality, consistency, and accuracy

Data deliverables are as good as their underlying data. Key component in this proposal is the source data gathering system.


## Data ingestion

Data Validation step is a process where the system performs quality tests on the submited data to

* Detect and fix human errors.
* Detect and fix broken automated sources.
* Notify the right people to address any issue on time.


## Data collection and Data Warehouse

The sink where the submitted data is stored serves as a data lake and the source of the Data Warehouse. 

* Data integration of common entities across different platforms.
* Data cleaning and data augmentation that adds value and increases its usefulness

## Data Marts and Visualization tools

Tailor-made data sets for the users to focus on nothing else but the data they nedd.

* Scheduled reports in different formats,
* Browsable data dashboards with data alerts or user notifications,
* Data ready to be analyzed across sources.

## Technology and cost

Several options are available for the implementation.

* Data ingestion can benefit from low-cost storage services like AWS S3 or GCP Cloud storage. 
* ETL processes can be a combination of native cloud services or custom-made scripts to pull data from the data sources. A balance of cost-benefit should be made.
* Cloud native logging services and dashboards saves us time in monitoring system health.
* Data Warehouse can benefit from low-cost cloud services like GCP Big Query or AWS Redshift while having a managed database for high priority and compatibility with end-user BI tools.