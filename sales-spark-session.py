'''Initializing the Spark-Mongo Connector'''

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MongoDB_to_DataFrame") \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:10.2.0") \
    .getOrCreate()

spark.conf.set("spark.mongodb.input.uri", "mongodb://mongo1:27017,mongo2:27018,mongo3:27019/Stocks.Source?replicaSet=rs0")
spark.stop()



'''Loading data as DataFrame using Spark'''

from pyspark.sql import SparkSession

url = 'mongodb://mongo1:27017,mongo2:27018,mongo3:27019/Stock.Price?replicaSet=rs0'
spark = (SparkSession
         .builder
         .master('local[*]')
         .config('spark.driver.extraClassPath','/home/jovyan/.ivy2/jars/*')
         .config("spark.mongodb.read.connection.uri",url)
         .config("spark.mongodb.write.connection.uri", url)
         .getOrCreate()
         )
df = spark.read.format("mongodb").option("collection", "fruits").option("database", "sales").load()
print('Anzahl der Daten:', df.count())
df.show()
spark.stop()







    
    


