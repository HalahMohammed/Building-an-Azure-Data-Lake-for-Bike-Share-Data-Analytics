# Building-an-Azure-Data-Lake-for-Bike-Share-Data-Analytics

## Project Overview :
This project implements a comprehensive data lake solution for Divvy bikeshare data using Azure Databricks and Delta Lake architecture. The solution processes anonymized bike trip data from Chicago's Divvy bikeshare program along with generated rider profiles and payment information to create an analytical data warehouse optimized for business intelligence and reporting.

## Business Context :
Divvy is a bike sharing program in Chicago that allows riders to:

- Purchase passes at kiosks or via mobile applications

- Unlock bikes from stations across the city

- Use bikes for specified time periods

- Return bikes to the same or different stations

- The City of Chicago provides anonymized trip data, which we've enhanced with synthetic rider profiles and payment information for analytical purposes.

## Data Architecture :

- Bronze Layer (Raw Data)
- Silver Layer (Cleaned Data)
- Gold Layer (Business-ready Data)

# Data Model :

The solution processes the following tables:

# Source Tables:

Rider: Fake rider profiles (synthetic data)

Account: Fake account information (synthetic data)

Payment: Fake payment transaction data (synthetic data)

Trip: Actual Divvy bikeshare trip data

Station: Bike station location and information

# Target Star Schema:

- Fact Tables: Trip facts, Payment facts

- Dimension Tables: Date, Rider, Station, Account, Time



Apache Spark 3.0+

Delta Lake
