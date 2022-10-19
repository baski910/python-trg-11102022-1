from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("sample").getOrCreate()

data = [1,2,3,4,5,6,7,8,9,10]

rdd = spark.sparkContext.parallelize(data)

#print(rdd.first())

print(rdd.take(2))

