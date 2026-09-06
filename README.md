# 🚕 Real-Time Cab Booking Data Pipeline

An end-to-end **real-time data engineering pipeline** for processing cab-booking events using **FastAPI, Azure Event Hubs, Azure Databricks, PySpark, Delta Lake, and Azure Data Lake Storage**.

The project simulates cab-booking transactions, streams events through Azure Event Hubs, processes them using Databricks, and transforms the data into structured and analytics-ready datasets using a **Medallion-style architecture**.

---

## 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │   FastAPI Web App     │
                         │  Cab Booking System   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Azure Event Hubs    │
                         │   Event Ingestion     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Azure Databricks    │
                         │  Spark / Lakeflow     │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────▼────────────────┐
                    │           Bronze               │
                    │       Raw Ride Events         │
                    └───────────────┬────────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │           Silver              │
                    │    Staging & Transformations  │
                    └───────────────┬───────────────┘
                                    │
                ┌───────────────────┼───────────────────┐
                ▼                   ▼                   ▼
        ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
        │ dim_passenger│    │  dim_driver  │    │ dim_payment  │
        └──────────────┘    └──────────────┘    └──────────────┘
                │                   │                   │
                └───────────────────┼───────────────────┘
                                    │
                         ┌──────────┴──────────┐
                         ▼                     ▼
                  ┌──────────────┐      ┌──────────────┐
                  │ dim_vehicle  │      │ dim_booking  │
                  └──────────────┘      └──────────────┘
```
## 🚀 Data Flow

### 1. Cab Booking Application

A **FastAPI** application provides the cab-booking interface.

When a booking is created, the application generates a synthetic ride event containing information such as:

- Passenger details
- Driver details
- Vehicle information
- Pickup and drop-off locations
- Ride status
- Payment method
- Fare information
- Ride timestamps
- Cancellation information
- Ride rating

### 2. Event Streaming

The generated booking event is serialized as JSON and published to **Azure Event Hubs**.

Azure Event Hubs acts as the event ingestion layer between the application and the data processing platform.

### 3. Bronze Layer

Raw ride events and reference datasets are ingested into **Delta tables**.

The Bronze layer preserves source data with minimal transformation and provides the foundation for downstream processing.

### 4. Silver Layer

The raw ride events are parsed using an explicit **PySpark schema** and transformed into structured records.

The data is enriched using lookup/reference datasets including:

- Cities
- Vehicle types
- Vehicle makes
- Payment methods
- Ride statuses
- Cancellation reasons

The resulting `silver_obt` dataset provides a consolidated representation of the processed ride data.

### 5. Dimension Processing

The Silver dataset is used to populate downstream dimension tables:

- `dim_passenger`
- `dim_driver`
- `dim_payment`
- `dim_vehicle`
- `dim_booking`

These transformations are executed as part of the **Azure Databricks pipeline**.
