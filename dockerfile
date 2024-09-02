# Use the official Apache Airflow image
FROM apache/airflow:2.6.3-python3.9

# Set environment variables
ENV AIRFLOW_HOME=/opt/airflow

# Copy your DAGs and data into the Airflow directory
COPY ./dags /opt/airflow/dags
COPY ./data /opt/airflow/data

# Install any additional dependencies
RUN pip install snowflake-connector-python Faker

# Set the working directory
WORKDIR /opt/airflow

# Initialize Airflow database and create user
RUN airflow db init && \
    airflow users create \
        --username admin \
        --password admin \
        --firstname Admin \
        --lastname User \
        --role Admin \
        --email admin@example.com

# Expose the necessary ports
EXPOSE 8080

# Start the Airflow webserver and scheduler
CMD ["bash", "-c", "airflow scheduler & airflow webserver"]
