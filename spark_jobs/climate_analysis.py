from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def main():
    spark = SparkSession.builder \
        .appName("Climate Data Analysis") \
        .getOrCreate()

    # Load data
    df = spark.read.csv("hdfs://namenode:9000/data/climate_data.csv", header=True)

    # Example transformation: Calculate average temperature
    avg_temp = df.groupBy("year").avg("temperature")
    avg_temp.show()

    spark.stop()

if __name__ == "__main__":
    main()
