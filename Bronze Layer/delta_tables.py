payments_columns = ['payment_id', 'date', 'amount', 'rider_id']

df = spark.read.format('csv') \
    .option('inferSchema', 'false') \
    .option('header', 'false') \
    .load('dbfs:/FileStore/payments.csv') \
    .toDF(*payments_columns)

# Write with mergeSchema to handle schema evolution
df.write.format('delta') \
    .option("mergeSchema", "true") \
    .mode('overwrite') \
    .save('/FileStore/delta_payments')
display(df)
df=spark.read.format('delta').option('header', 'true').load('/FileStore/delta_payments')
df.write.format('delta').saveAsTable('delta_table')

rider_columns=['rider_id','first','last','address','birthday','account_start_date','account_end_date','is_member']
df=spark.read.format('csv')\
.option('header','false')\
.option('inferSchema','false')\
.load('dbfs:/FileStore/riders.csv')\
.toDF(*rider_columns)
df.write.format('delta').option('mergeSchema','true').mode('overwrite').save('/FileStore/delta_riders')
df.display()
df=spark.read.format('delta').option('header', 'true').load('/FileStore/delta_riders')
df.write.format('delta').saveAsTable('rider_table')

station_columns=['station_id','name','latitude','longitude'] 
df=spark.read.format('csv')\
.option('header','false').\
option('inferSchema','false')\
.load('dbfs:/FileStore/stations.csv')\
.toDF(*station_columns)
df.write.format('delta').save('/FileStore/delta_stations')
df.display()
df=spark.read.format('delta').option('header', 'true').load('/FileStore/delta_stations')
df.write.format('delta').saveAsTable('station_table')


trip_columns=['trip_id','rideable_id','started_at','ended_at','start_station_id','end_station_id','rider_id']
df=spark.read.format('csv').option('inferSchema','false').option('header','false').load('dbfs:/FileStore/trip.csv').toDF(*trip_columns)
df.write.format('delta').option('mergeSchema','true').mode('overwrite').save('/FileStore/delta_trip')
df.display()
df=spark.read.format('delta').option('header', 'true').load('/FileStore/delta_trip')
df.write.format('delta').saveAsTable('trip_table')
