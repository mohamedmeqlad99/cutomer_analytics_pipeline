Customer Analytics Pipeline
============================

Project Description
--------------------
This project is a customer analytics data pipeline built using **Apache Airflow** for orchestration, **Snowflake** as the data warehouse, and **Python** for data visualization. The pipeline generates fake customer data using **Faker**, loads it into Snowflake, and provides visual insights via Python using **Matplotlib**, **Seaborn**, and **Plotly**.

The data consists of customer information, including `customer_id`, `first_name`, `last_name`, `email`, `phone_number`, `address`, and `date_of_birth`.

Technologies Used:
- Airflow: Orchestrates the data pipeline.
- Snowflake: Stores customer data.
- Faker: Generates synthetic customer data.
- Docker: Manages the environment and dependencies for Airflow.
- Python: Creates data visualizations and connects to Snowflake.
- Matplotlib, Seaborn, Plotly: Visualizes customer data.

  ![image](https://github.com/user-attachments/assets/ee831ccd-d30a-42dc-9cfa-0b9ebfc1eaaf)


Setup Instructions
--------------------
Prerequisites:
1. Docker: Install from https://www.docker.com/get-started.
2. Airflow: The setup uses Docker to run Airflow, so no additional installation is required.
3. Snowflake: Create a Snowflake account and set up a warehouse, database, and schema.

Step 1: Clone the Repository
-----------------------------
```bash
git clone https://github.com/your-username/customer_analytics_pipeline.git
cd customer_analytics_pipeline
