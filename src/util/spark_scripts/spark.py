#create dataframe
spark.createDataFrame(df[['col', 'col2', 'col3']])

#create view
df.createOrReplaceGlobalTempView('nameofview')

#read global view
spark.table('global_temp.nameofview')

#connect to table
spark.table('')

df.select('column').count()

# filters
df[
    (df['column'].isNull()) |
    (df['column'].isNull())
]

df.filter(df['column'].startswith('d'))

#groupby
df.groupby('col').count()

df.groupby('col').count().sort('count').show()

# joins
df1.alias('df1'). join(df2.alias('df2'), on = df1['col'] == df2['col'], how = 'inner')

#merge
df.merge(df2 , left_on='col', right_on='col2', how = 'inner')

#union
df1.union(df2)

#replace with
df[df['col'] < 1000] = 0

#collect
df.select('column')collect[0][0]

#to pandas
df.toPandas()

#displays
displayHTML('')

#latest date
df.select('date').distinct().sort(desc('date')).collect()[0]
