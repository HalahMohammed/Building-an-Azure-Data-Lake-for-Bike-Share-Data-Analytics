column_names=['station_id','name','latitude','longitude'] 
df=spark.read.format('csv')\
.option('header','false').\
option('inferSchema','false')\
.load('dbfs:/FileStore/stations.csv')\
.toDF(*column_names)
df.write.format('delta').save('/FileStore/delta_stations')
df.display()
