
import pendulum
import pandas as pd
import httpx
import pandera.pandas as pa
from pandera.typing import Series
import pyarrow
import os
import sys
import logging

# Setting up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def main():
    # Extract data, normalize json and show 5 first rows
    all_results = []
    skip = 0
    limit = 100
    start_date = pendulum.parse('2025-08-01')
    end_date = pendulum.parse('2025-08-31')

    logging.info('Starting data extraction from OpenFDA API...')
    while start_date <= end_date:
        logging.info(f'Processing date: {start_date}')
        skip = 0
        while True:
            try:
                url = f"https://api.fda.gov/drug/event.json?search=receivedate:[{start_date.format('YYYYMMDD')}+TO+{start_date.format('YYYYMMDD')}]&limit={limit}&skip={skip}"
                logging.info(f'Fetching data from URL: {url}')
                response = httpx.get(url)
                response.raise_for_status()
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 404:
                    logging.warning(f'No data found for date: {start_date}')
                    break
                else:
                    logging.error(f'Error fetching data: {e}')
                raise
            else:
                data = response.json()
                page_results = data.get("results", [])
                logging.info(f"Fetched {len(page_results)} records, total so far: {len(all_results)}")
                if len(page_results) == 0:
                    break
                all_results.extend(page_results)
                skip += limit
        start_date = start_date.add(days=1)
        df = pd.json_normalize(all_results)
        logging.info(df.head())
            
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
            
if __name__ == "__main__":
    main()