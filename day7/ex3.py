from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("sample").getOrCreate()

df = spark.read.format("csv").option("header","true").option("inferSchema","true").load("uk-500.csv")

#df.select("first_name","last_name").show() # display first 20 rows

#df.select("first_name","last_name").show(30) # display first 30 rows
#print()
#df.select("first_name","last_name").show(df.count())

#df.filter("first_name=='France'").show()

#df.filter(df.first_name.like("%Marg%")).show() # search rows containing 'Marg' in first_name
df.filter(df.first_name.rlike("^.*Marg.*")).show()