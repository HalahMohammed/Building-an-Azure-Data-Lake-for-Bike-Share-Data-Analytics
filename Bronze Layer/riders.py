
column_names=['rider_id','first','last','address','birthday','account_start_date','account_end_date','is_member']

df=spark.read.format('csv')\
.option('header','false')\
.option('inferSchema','false')\
.load('dbfs:/FileStore/riders.csv')\
.toDF(*column_names)
df.write.format('delta').option('mergeSchema','true').mode('overwrite').save('/FileStore/delta_riders')
df.display()

df=spark.read.format('delta').option('header', 'true').load('/FileStore/delta_riders')
df.write.format('delta').saveAsTable('rider_table')
