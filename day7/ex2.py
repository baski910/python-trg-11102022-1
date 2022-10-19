from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("sample").getOrCreate()

rdd = spark.sparkContext.textFile("readme.txt")

# fh.readlines()

#print(rdd.collect())

#for element in rdd.collect():
#    print(element)

rdd2 = rdd.flatMap(lambda x: x.split(" "))

#print(rdd2.collect())

rdd3 = rdd2.map(lambda x: (x,1))

#print(rdd3.collect())

rdd4 = rdd3.reduceByKey(lambda a,b: a+b)

print(rdd4.collect())

# rdd2 = rdd.flatMap(lambda x: x.split(" ")).map(lambda x: (x,1)).reduceByKey(lambda a,b: a+b)