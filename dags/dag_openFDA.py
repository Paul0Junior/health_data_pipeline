from airflow.decorators import dag, task
import pendulum
import pandas as pd
import duckdb
import httpx
import pandera.pandas as pa
from pandera.typing import Series
import pyarrow
import duckdb
import os
import sys
import logging

# Configurando logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

@dag(
    dag_id='dag_OpenFDA',
    schedule=None,
    start_date=pendulum.datetime(2025, 1, 1, tz='GMT'),
    catchup=False,
    tags=['openfda']
)

def fda_pipeline():
    @task
    def  extract_validate():
        # Extract data, normalize json and show 5 first rows
        try:
            logging.info('Extracting data...')
            response = httpx.get('https://api.fda.gov/drug/event.json?search=serious:1&limit=10')
        except Exception as e:
            raise
        else:
            logging.info('Data extracted successfully.')
        data = response.json() 
        df = pd.json_normalize(data['results'])
        df.head()

        # Set the schema for validation:
        schema = pa.DataFrameSchema(
            columns={
                "serious": pa.Column(int, coerce=True),
                "receiver.receiverorganization": pa.Column(str, nullable=True),
                "patient.patientsex": pa.Column(int, nullable=True, coerce=True)
            },
            strict="filter" # Ignore columns not in the schema
        )

        # Build the validated dataframe:
        validated_df = schema.validate(df)
        
        # Store the validated dataframe as a .parquet file
        folder = '/opt/airflow/Data/OpenFDA'
        if not os.path.exists(folder):
            os.makedirs(folder)
        try:
            logging.info('Saving .Parquet file...')
            validated_df.to_parquet(f"{folder}/adverse_events.parquet", engine='pyarrow')
        except Exception as e:
            raise
        else:
            logging.info('.Parquet file saved successfully.')

    @task
    def sumarize_data():
        folder ='/opt/airflow/Data/OpenFDA'
        file_path=f'{folder}/adverse_events.parquet'

        query = f"""
            SELECT 
                "patient.patientsex",
                COUNT(*) as total_events,
            FROM read_parquet('{file_path}')
            GROUP BY "patient.patientsex"
        """

        sumary_df = duckdb.query(query).to_df()
        print('Events summary by patient sex')
        print(sumary_df)

    extract_validate() >> sumarize_data()

fda_pipeline()