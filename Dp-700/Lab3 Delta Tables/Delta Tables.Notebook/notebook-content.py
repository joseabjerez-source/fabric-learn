# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "14966ec9-fc55-413a-9041-278c5bf0820a",
# META       "default_lakehouse_name": "Lab3LH",
# META       "default_lakehouse_workspace_id": "2a48cce1-1ba4-4ca4-b69b-3bbd223c5f3d",
# META       "known_lakehouses": [
# META         {
# META           "id": "14966ec9-fc55-413a-9041-278c5bf0820a"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Welcome to your new notebook
# # Type here in the cell editor to add code!


# CELL ********************

from pyspark.sql.types import StructType, IntegerType, StringType, DoubleType

schema = StructType() \
.add("ProductID", IntegerType(), True) \
.add("ProductName", StringType(), True) \
.add("Category", StringType(), True) \
.add("ListPrice", DoubleType(), True)

df = spark.read.format("csv").option("header", "true").schema(schema).load("Files/products/products.csv")

display(df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.format("delta").saveAsTable("managed_products")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.format("delta").saveAsTable("external_products", path="abfss://2a48cce1-1ba4-4ca4-b69b-3bbd223c5f3d@onelake.dfs.fabric.microsoft.com/14966ec9-fc55-413a-9041-278c5bf0820a/Files/external_products")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC DESCRIBE FORMATTED managed_products;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC DESCRIBE FORMATTED external_products;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC CREATE TABLE products
# MAGIC USING DELTA
# MAGIC LOCATION 'Files/external_products';


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
