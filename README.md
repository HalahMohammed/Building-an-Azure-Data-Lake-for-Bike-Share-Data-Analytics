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

## Data Model :

The dataset consists of the following tables:

## Dimension Tables

Riders: Rider demographic information and membership details

Stations: Bike station locations and details

Date: Time dimension for temporal analysis

## Fact Tables :

Trips: Bike trip transactions with duration and routing

Payments: Payment transactions linked to riders

