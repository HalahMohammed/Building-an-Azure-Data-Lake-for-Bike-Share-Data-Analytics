
column_names=['trip_id','rideable_id','started_at','ended_at','start_station_id','end_station_id','rider_id']
df=spark.read.format('csv').option('inferSchema','false').option('header','false').load('dbfs:/FileStore/trip.csv').toDF(*column_names)

df.write.format('delta').option('mergeSchema','true').mode('overwrite').save('/FileStore/delta_trip')
df.display()

df=spark.read.format('delta').option('header', 'true').load('/FileStore/delta_trip')
df.write.format('delta').saveAsTable('trip_table')
