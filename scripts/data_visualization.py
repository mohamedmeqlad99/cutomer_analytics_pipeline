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

# -- plot date of birth --
plt.figure(figsize=(10, 6))
sns.histplot(df['date_of_birth'], bins=20, kde=False)
plt.title('Customer Birth Year Distribution')
plt.xlabel('Date of Birth')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# -- plot email domains --

df['email_domain'] = df['email'].apply(lambda x: x.split('@')[-1])  # Extract email domain
email_domain_counts = df['email_domain'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=email_domain_counts.index, y=email_domain_counts.values)
plt.title('Top 10 Email Domains')
plt.xlabel('Email Domain')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# -- end of visualization --
