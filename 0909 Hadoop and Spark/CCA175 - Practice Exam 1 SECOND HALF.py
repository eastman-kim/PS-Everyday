#!/usr/bin/env python
# coding: utf-8

# ### Practice 1 - Question 5

# `Instructions`
# - Convert avro data-files stored at hdfs location /user/cloudera/practice1/problem7/customer/avro  into tab delimited file
# 
# 
# 
# `Output Requirement`
# 
# - Result should be saved in /user/cloudera/practice1/problem7/customer_text_bzip2
# - Output file should be saved as tab delimited file in bzip2 Compression.
# - Output should consist of customer_id, customer_fname(only first three letter), customer_lname
# 

# In[ ]:


#load data as dataframe
customers = spark.read.format("avro").load("/user/cloudera/practice1/problem/customers/avro")

#create temp view
customers.createorReplaceTempView("customers")

#run the sql query
customersFiltered = spark.sql("select concat(customer_id,"\t", substr(customer_fname,0,3),"\t", customer_lname) from customers")
                            
#save the dataframe
customersFiltered.write.option("compression","bzip2").format("text").save("/user/cloudera/practice1/problem7/output")


# ### Practice 1 - Question 6

# `Instructions`
# - Get products from metastore table named "product_replica" whose price > 100 and save the results in HDFS in parquet format.
# 
# 
# 
# `Output Requirement`
# - Result should be saved in /user/cloudera/practice1/problem8/product/output as parquet file
# - Files should be saved in uncompressed format.
# 

# In[ ]:


spark.sql("select * from product_replica where product_price>100").write.option("compression","uncompressed").format("parquet").save("/user/cloudera/practice1/problem8/product/output")


# ### Practice 1 - Question 7

# `Instructions`
# - Find out all PENDING_PAYMENT orders in March 2014.
# - order_date format is in unix_timestamp
# - Input file is parquet file stored at hdfs location /user/cloudera/practice1/question8
# 
# 
# `Output Requirement`
# - Output should be date and total pending order for that date.
# - Output should be saved at below hdfs location /user/cloudera/practice1/question8/output
# - Output should be json file format.

# In[ ]:


#load data as dataframe
orders = spark.read.format("parquet").load("/user/cloudera/practice1/problem8/")

#filter data
from pyspark.sql.functions import from_unixtime
from pyspark.sql.functions import to_date

ordersFiltered = orders.withColumn("order_date", to_date(from_unixtime(orders.order_date/1000)))
ordersFilteredYear = ordersFiltered.filter(orders.order_date.like("2014-03%"))
ordersFilteredStatus = ordersFilteredYear.filter(orders.order_status=="PENDING_PAYMENT")

#create temp view
ordersFilteredStatus.createorReplaceTempView("ordersFiltered")

#run the sql query
ordersGroupByOrderDate = spark.sql("select order_date, count(*) as count from ordersFiltered group by order_date")

#save the dataframe
ordersGroupByOrderDate.write.json("/user/cloudera/practice1/problem8/output")


# ### Practice 1 - Question 8

# `Instructions`
# - Find out total number of orders placed by each customers in year 2013.
# - Order status should be COMPLETE
# - order_date format is in unix_timestamp
# - Input customer & order files are stored as avro file at below hdfs location 
#     - /user/cloudera/practice2/question8/orders
#     - /user/cloudera/practice2/question8/customers
# 
# 
# `Output Requirement`
# - Output should be stored in a hive table named "customer_order" with three columns customer_fname,customer_lname and orders_count.

# In[2]:


#load data as dataframe
orders = spark.read.format("avro").load("/user/cloudera/practice1/problem8/orders")
customers = spark.read.format("avro").load("/user/cloudera/practice1/problem8/customers")


#filter data
from pyspark.sql.functions import from_unixtime
from pyspark.sql.functions import to_date

ordersFiltered = orders.withColumn("order_date", to_date(from_unixtime(orders.order_date/1000)))
ordersFilteredYear = ordersFiltered.filter(orders.order_date.like("2013%"))
ordersFilteredStatus = ordersFilteredYear.filter(orders.order_status=="COMPLETE")
ordersFilteredFinal = ordersFilteredStatus.selectExpr("order_id", "order_date","order_customer_id as customer_id")
customers = customers.select("customer_id,customer_fname", "customer_lname", "customer_state")

#create temp view
ordersFilteredStatus.createorReplaceTempView("ordersFiltered")

#run the sql query
ordersGroupByCustomerId = spark.sql("select customer_id, count(*) as order_count from ordersFiltered group by customer_id")

#join two datasets
ordersCustomersJoin = ordersGroupByCustomerId.join(customers, "customer_id")
result = ordersCustomersJoin.select("customer_fname","customer_lname","order_count","customer_state")
#save the dataframe in Hive
result.write.partitionBy("customer_state").format("hive").saveAsTable("customer_order")

