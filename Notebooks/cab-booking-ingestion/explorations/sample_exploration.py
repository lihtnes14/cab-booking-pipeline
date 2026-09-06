# Databricks notebook source

from pyspark.sql.functions import *
from pyspark.sql.types import *

# Event Hubs configuration
EH_NAMESPACE = "booking-events"
EH_NAME = "bookingtopic"


EH_CONN_STR = "Endpoint=sb://booking-events.servicebus.windows.net/;SharedAccessKeyName=ListenPolicy;SharedAccessKey=lOGZaJXr76RmIDeCBTXlOLfUoFBHCd1nW+AEhJ47raY=;EntityPath=bookingtopic"

KAFKA_OPTIONS = {
  "kafka.bootstrap.servers"  : f"{EH_NAMESPACE}.servicebus.windows.net:9093",
  "subscribe"                : EH_NAME,
  "kafka.sasl.mechanism"     : "PLAIN",
  "kafka.security.protocol"  : "SASL_SSL",
  "kafka.sasl.jaas.config"   : f"kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required username=\"$ConnectionString\" password=\"{EH_CONN_STR}\";",
  "kafka.request.timeout.ms" : 10000,
  "kafka.session.timeout.ms" : 10000,
  "maxOffsetsPerTrigger"     : 10000,
  "failOnDataLoss"           : "true",
  "startingOffsets"          : "earliest"
}

df = spark.readStream.format('kafka')\
                .options(**KAFKA_OPTIONS)\
                .load()
                
df = df.withColumn("rides", col("value").cast(StringType()))

display(df, checkpointLocation = "/Volumes/cab-booking/bronze/my_volume")

# COMMAND ----------

