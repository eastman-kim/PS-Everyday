#!/usr/bin/env python
# coding: utf-8

# ### Practice 1 - Question 1

# `Instructions`
# - Convert snappy compressed avro data-files stored at hdfs location /user/cloudera/practice1/question3  into parquet file.
# - open pyspark/spark-shell with --packages org.apache.spark:spark-avro_2.12:2.4.5
# 
# 
# 
# `Output Requirement`
# 
# - Result should be saved in /user/cloudera/practice1/question3/output/
# - Output should consist of only order_id,order_status
# - Output file should be saved as Parquet file in gzip Compression.
# 

# In[ ]:


#load data as dataframe
orders = spark.read.format("avro").load("/user/cloudera/practice1/question3")

#save the dataframe
orders.select("order_id","order_status").write.option("compression","gzip") .format("parquet").save("/user/cloudera/practice1/question3/output")


# ### Practice 1 - Question 2

# `Instructions`
# - Join the comma separated file located at hdfs location /user/cloudera/p1/p4/orders & /user/cloudera/p1/p4/customers to find out  customers who have placed more than 4 orders.
# 
# 
# 
# `Output Requirement`
# - Order status should be COMPLETE
# - Output should have customer_id,customer_fname,count
# - Save the results in json format.
# - Result should be order by count of orders in ascending fashion.
# - Result should be saved in /user/cloudera/p1/p4/output 
# 

# In[ ]:


#load data as dataframe
customers = spark.read.format("csv").load("/user/cloudera/p1/p4/customers")
orders = spark.read.format("csv").load("/user/cloudera/p1/p4/orders")

#rename columns
customers = customers.selectExpr("_c0 as customer_id", "_c1 as customer_fname")
orders = orders.selectExpr("_c2 as customer_id", "_c3 as order_status")

#create temp view
orders.createorReplaceTempView("orders")

#run the sql query
customersGroupByCustomerId = spark.sql("select customer_id, count(*) as count from orders                                        group by customer_id having count>4 order by count desc")

#join two dataframes
customersGroupByCustomerId.join(customers, "customer_id").write.json("/user/cloudera/p1/p4/output")


# ### Practice 1 - Question 3

# `Instructions`
# - From provided parquet files located at hdfs location : /user/cloudera/practice1/problem5
# - Get maximum product_price in each product_category
# - order the results by maximum price descending.
# 
# 
# `Output Requirement`
# - Final output should be saved in below hdfs location: /user/cloudera/practice1/problem5/output
# - Final output should have product_category_id and max_price separated by pipe delimiter
# - Ouput should be saved in text format with Gzip compression
# - Output should be stored in a single file.

# In[ ]:


#load data as dataframe
products = spark.read.format("parquet").load("/user/cloudera/practice1/problem5/")

#create temp view
products.createorReplaceTempView("products")

#run the sql query
productsMaxPricePerCategoryId = spark.sql("select concat(product_category_id,'|', max(product_price)) from products                                        group by product_category_id order by max(product_price) desc")
#save the dataframe
productsMaxPricePerCategoryId.coalesce(1).write.option("compression","gzip").format("text").save("/user/cloudera/practice1/problem5/output")


# ### Practice 1 - Question 4

# `Instructions`
# - Provided customer tab delimited files at below HDFS location.
# - Input folder is  /user/cloudera/practice1/problem6
# - Find all customers that lives 'Caguas' city.
# 
# 
# `Output Requirement`
# - Result should be saved in /user/cloudera/practice1/problem6/output
# - Output file should be saved in avro format in deflate compression.

# In[ ]:


#load data as dataframe
customers = spark.read.option("sep","\t").format("csv").load("/user/cloudera/practice1/problem6/")

#create temp view
customers.createorReplaceTempView("customers")

#run the sql query
customersCaguas = spark.sql("select * from customers where customer_city = 'Caguas'")
                            
#save the dataframe
customersCaguas.write.option("compression","deflate").format("avro").save("/user/cloudera/practice1/problem6/output")

