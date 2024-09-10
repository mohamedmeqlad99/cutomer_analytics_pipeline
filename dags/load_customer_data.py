from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from datetime import datetime

# Define the Snowflake connection ID
SNOWFLAKE_CONN_ID = 'snowflake_default'

# Define the hook parameters for Snowflake
hook_params = {
    'warehouse': '<your_snowflake_warehouse>',
    'database': '<your_snowflake_database>',
    'schema': '<your_snowflake_schema>',
    'role': '<your_snowflake_role>',
}

# Define the DAG
with DAG(
    dag_id='load_customer_data_to_snowflake',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:
    
    # Task to create the Snowflake table
    create_table = SQLExecuteQueryOperator(
        task_id='create_snowflake_table',
        conn_id=SNOWFLAKE_CONN_ID,
        sql="""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id STRING,
                first_name STRING,
                last_name STRING,
                email STRING,
                phone_number STRING,
                address STRING,
                date_of_birth DATE
            );
        """,
        hook_params=hook_params,
    )
    
    # Task to load data into Snowflake
    load_data = SQLExecuteQueryOperator(
        task_id='load_data_to_snowflake',
        conn_id=SNOWFLAKE_CONN_ID,
        sql="""
            INSERT INTO customers (customer_id, first_name, last_name, email, phone_number, address, date_of_birth)
            SELECT customer_id, first_name, last_name, email, phone_number, address, date_of_birth
            FROM '@/opt/airflow/data/customer_data.csv';
        """,
        hook_params=hook_params,
    )
    
    create_table >> load_data
