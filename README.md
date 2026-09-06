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
