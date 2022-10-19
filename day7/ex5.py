from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("sample").getOrCreate()

empData = [
    ("bob","sales",2500),
    ("raj","sales",4000),
    ("tom","finance",5200),
    ("joe","Accounts",4000),
    ("pat","sales",5000),
    ("mahi","Accounts",6000),
    ("sam","finance",4000)
]
schema = ["employee_name","department","salary"]
df = spark.createDataFrame(data=empData, schema=schema)
#df.show()
#print(df.select(avg("salary")).collect())
#df.groupby("department").sum("salary").show()
#g = df.groupby("department").sum("salary") 
#g.write.csv("results") # creates a directory named 'results' and then create csv inside