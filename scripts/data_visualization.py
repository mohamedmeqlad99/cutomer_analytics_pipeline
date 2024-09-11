import pandas as pd
import snowflake.connector
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#  credentials
conn = snowflake.connector.connect(
    user='<your_snowflake_user>',
    password='<your_snowflake_password>',
    account='<your_snowflake_account>',
    warehouse='<your_snowflake_warehouse>',
    database='<your_snowflake_database>',
    schema='<your_snowflake_schema>'
)

query = "SELECT * FROM customers"

df = pd.read_sql(query, conn)

conn.close()
