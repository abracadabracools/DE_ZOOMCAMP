#!/usr/bin/env python
# coding: utf-8

# This file was tested with MacOS using Conda for Python management.
# 
# Make sure that your Python env has `pandas` and `sqlalchemy` installed. I also had to install `psycopg2` manually.

import pandas as pd
from sqlalchemy import create_engine

# We will start by reading a small sample of the CSV file to get an idea of its structure.
df = pd.read_csv('yellow_tripdata_2021-01.csv', nrows=100)

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

# run this cell when the Postgres Docker container is running
engine.connect()


# we can now use our engine to get the specific output for Postgres
# print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))

df_iter = pd.read_csv('yellow_tripdata_2021-01.csv', iterator=True, chunksize=100000)

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)


# we need to provide the table name, the connection and what to do if the table already exists
# we choose to replace everything in case you had already created something by accident before.
df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')
df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')
from time import time

while True: 
    try:
        t_start = time()
        df = next(df_iter)

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        
        df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')

        t_end = time()

        print('inserted another chunk, took %.3f second' % (t_end - t_start))
    except StopIteration:
        print('completed')
        break


# And that's it! Feel free to go back to the [notes](../notes/1_intro.md#inserting-data-to-postgres-with-python)
