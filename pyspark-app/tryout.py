from pyspark.sql import SparkSession

# Create SparkSession 
spark = SparkSession.builder \
      .master("127.0.0.1:7077") \
      .appName("SparkByExamples.com") \
      .getOrCreate()
