# Databricks notebook source
import pandas as pd

url = "https://dlcabbookdev.blob.core.windows.net/raw/ingestion/map_cities.json"

base_url = "https://dlcabbookdev.blob.core.windows.net/raw"
sas_token = "https://dlcabbookdev.blob.core.windows.net/?sv=2026-02-06&ss=bfqt&srt=c&sp=rwdlacupiytfx&se=2026-08-30T21:46:49Z&st=2026-08-25T13:31:49Z&spr=https&sig=eo9VIoPiq8s0BMyRvZTwkwqoE%2BgsbVFqJ2RD8bJ52s8%3D"

files_url = "https://dlcabbookdev.blob.core.windows.net/raw/files_array.json?sp=r&st=2026-08-25T14:01:41Z&se=2026-08-25T22:16:41Z&spr=https&sv=2026-02-06&sr=c&sig=9GLFdzU8a1CB11UrGYGPgBcGPi0VoPCLraxHTSDxvB0%3D"





# COMMAND ----------

import pandas as pd

df = pd.read_json(
    "https://dlcabbookdev.blob.core.windows.net/raw/ingestion/map_cities.json?sv=2026-02-06&ss=bfqt&srt=co&sp=rwdlacupiytfx&se=2026-08-25T22:22:24Z&st=2026-08-25T14:07:24Z&spr=https&sig=2RnUlaqdvLWClMVI4RtLB0ubD5FpFYILxLXwYZmkwb8%3D"
)

df_spark = spark.createDataFrame(df)

display(df_spark)

# COMMAND ----------



# COMMAND ----------

import pandas as pd

base_url = "https://dlcabbookdev.blob.core.windows.net/raw"

sas_token = "sp=r&st=2026-08-25T14:26:13Z&se=2026-08-25T22:41:13Z&spr=https&sv=2026-02-06&sr=c&sig=fUkRadjtyX5LJOA8p1tXMKGB0jMdKvBlOfiEOPZ35nk%3D"

# COMMAND ----------

import pandas as pd

files = [
    {"file":"map_cities"},
{"file":"bulk_rides"},
{"file":"map_cancellation_reasons"},
{"file":"map_payment_methods"},
{"file":"map_ride_statuses"},
{"file":"map_vehicle_makes"},
{"file":"map_vehicle_types"}
]
 


for file in files:
    url = f"{base_url}/ingestion/{file['file']}.json?{sas_token}"
    df = pd.read_json(url)
    df_spark = spark.createDataFrame(df)

    df_spark.write.format("delta")\
        .mode("overwrite")\
        .option("overwriteSchema", "true") \
        .saveAsTable(f"`cab-booking`.bronze.{file['file']}")

    

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM `cab-booking`.bronze.map_cities

# COMMAND ----------

