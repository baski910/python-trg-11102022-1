import pandas as pd
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("sample").getOrCreate()

df = pd.read_excel('test.xlsx',sheet_name='Sheet2',skiprows=1)
exceldata = df.values.tolist()

schema = ["first_name","last_name","email"]

df1 = spark.createDataFrame(data=exceldata, schema = schema)
df1.show()