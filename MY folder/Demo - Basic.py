# Databricks notebook source
print('Hello World')

# COMMAND ----------

# MAGIC %sql
# MAGIC select " Hello World from SQL!! "

# COMMAND ----------

# MAGIC %md
# MAGIC # Title 1
# MAGIC ##Title 2
# MAGIC ### Title 3

# COMMAND ----------

# MAGIC %run ./Databricks-Certified-Data-Engineer-Associate/Includes/Setup
# MAGIC

# COMMAND ----------

print("full_name is ",full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

##another way to deal with file system operations is to use dbutils command

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files=dbutils.fs.ls('/databricks-datasets')
print(files)
display(files)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------


