

column_names = ['payment_id', 'date', 'amount', 'rider_id']

df = spark.read.format('csv') \
    .option('inferSchema', 'false') \
    .option('header', 'false') \
    .load('dbfs:/FileStore/payments.csv') \
    .toDF(*column_names)

# Write with mergeSchema to handle schema evolution
df.write.format('delta') \
    .option("mergeSchema", "true") \
    .mode('overwrite') \
    .save('/FileStore/delta_payments')

display(df)

df=spark.read.format('delta').option('header', 'true').load('/FileStore/delta_payments')
df.write.format('delta').saveAsTable('delta_table')
