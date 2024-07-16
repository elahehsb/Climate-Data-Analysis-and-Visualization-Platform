from pyspark.ml import Pipeline
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("Climate Data ML Model") \
        .getOrCreate()

    # Load and preprocess data
    df = spark.read.csv("hdfs://namenode:9000/data/climate_data.csv", header=True)
    assembler = VectorAssembler(inputCols=["year", "month"], outputCol="features")

    # Split data
    (training_data, test_data) = df.randomSplit([0.7, 0.3])

    # Define model
    lr = LinearRegression(labelCol="temperature", featuresCol="features")

    # Build pipeline
    pipeline = Pipeline(stages=[assembler, lr])

    # Train model
    model = pipeline.fit(training_data)

    # Evaluate model
    predictions = model.transform(test_data)
    predictions.select("features", "temperature", "prediction").show()

    spark.stop()

if __name__ == "__main__":
    main()
