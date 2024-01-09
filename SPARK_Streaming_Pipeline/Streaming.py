import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col , from_csv
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml import Pipeline
from pyspark.ml.classification import RandomForestClassificationModel 


snowflake_options = {
    "sfUrl" : "yz51096.eu-west-3.aws.snowflakecomputing.com",
    "sfUser" : "username",
    "sfPassword" : "password", 
    "sfDatabase" : "CHURN",
    "sfSchema" : "CHURN",
    "sfRole" : "ACCOUNTADMIN",
    "sfWarehouse" : "COMPUTE_WH",
    "dbtable" : "CHURN"
}


# Create a Spark session
spark = SparkSession.builder.appName("ChurnStructuredStreaming").getOrCreate()

# Define the Kafka parameters
kafka_params = {
    "kafka.bootstrap.servers": "localhost:9092",
    "subscribe": "churn"
}

# Read data from Kafka as a DataFrame
raw_stream_df = (
    spark
    .readStream
    .format("kafka")
    .option("startingOffsets", "earliest")
    .options(**kafka_params)
    .load()
    .selectExpr("CAST(value AS STRING)")
)

#schema du dataframe
schema = "customerID STRING,gender STRING,SeniorCitizen INT,Partner STRING,Dependents STRING,tenure INT,PhoneService STRING,MultipleLines STRING,InternetService STRING,OnlineSecurity STRING,OnlineBackup STRING,DeviceProtection STRING,TechSupport STRING,StreamingTV STRING,StreamingMovies STRING,Contract STRING,PaperlessBilling STRING,PaymentMethod STRING,MonthlyCharges DOUBLE,TotalCharges STRING,Churn STRING"


def process_batch(batch_df, batch_id):
  
    # Parse CSV data

    #parsed_data = batch_df.select(from_json(col("value"), csv_schema).alias("data")).select("data.*")
    parsed_data = batch_df.select(from_csv(batch_df.value, schema).alias("data")).select("data.*")
    #df = spark.createDataFrame(parsed_data)


    
    # Supprimer la colonne 'customerID'
    parsed_data = parsed_data.drop("customerID")
    # Convertir 'TotalCharges' en numeric
    parsed_data = parsed_data.withColumn("TotalCharges", col("TotalCharges").cast("double"))
    # Supprimer les valeurs manquantes dans TotalCharges
    parsed_data = parsed_data.na.drop(subset=["TotalCharges"])
    #categories of data
    categorical_columns = ["gender", "Partner", "Dependents", "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod"]
    numerical_columns = ["SeniorCitizen", "tenure", "MonthlyCharges", "TotalCharges"]

    
    # Apply the transformations done during training
    indexers = [StringIndexer(inputCol=col, outputCol=f"{col}_index").fit(parsed_data) for col in categorical_columns]
    pipeline = Pipeline(stages=indexers)
    parsed_data = pipeline.fit(parsed_data).transform(parsed_data)
    feature_columns = [f"{col}_index" for col in categorical_columns] + numerical_columns
    assembler = VectorAssembler(inputCols=feature_columns, outputCol="features")
    parsed_data = assembler.transform(parsed_data)

    
    # Make predictions using the loaded Random Forest model
    predictions = loaded_rf_model.transform(parsed_data)

    # Output the Results
    #predictions.selectExpr("CAST(prediction AS double) AS key", "to_json(struct(*)) AS value")

    
    print("--"*50)
    predictions.select(['Churn', 'probability', 'prediction']).show()
    #parsed_data.show()

    predictions.select(['gender','SeniorCitizen','Partner','Dependents','tenure','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies', 'Contract', 'PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges','churn',  'prediction']).write.format("net.snowflake.spark.snowflake") \
    .option("sfUrl", snowflake_options["sfUrl"]) \
    .option("sfUser", snowflake_options["sfUser"]) \
    .option("sfPassword", snowflake_options["sfPassword"]) \
    .option("sfWarehouse", snowflake_options["sfWarehouse"]) \
    .option("sfRole", snowflake_options["sfRole"]) \
    .option("sfDatabase", snowflake_options["sfDatabase"]) \
    .option("sfSchema", snowflake_options["sfSchema"]) \
    .option("dbtable", snowflake_options["dbtable"]) \
    .mode("append") \
    .save()


#loading the model
loaded_rf_model = RandomForestClassificationModel.load("Model/random_forest_model")

# Define the streaming query
query = (
    raw_stream_df
    .writeStream
    .outputMode("append")
    .format("kafka")
    .foreachBatch(process_batch)  # Custom function to handle each batch
    .start()
)

# Await termination
query.awaitTermination()
