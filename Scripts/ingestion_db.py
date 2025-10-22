import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time


engine = create_engine("sqlite:///inventory.db")

def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists = "append",index=False)

def load_raw_data():
    start = time.time()
    for file in os.listdir("data"):
        if ".csv" in file:
            print(file)
            chunk_size = 1000
            chunks = []
            logging.info(f'Ingesting {file} in db')
            for chunk in pd.read_csv("data/"+file,chunksize=chunk_size):
                df=chunk
                ingest_db(df,file[:-4],engine)
    end = time.time()
    total_time = (end-start)/60
    logging.info(f'Total time Taken is {total_time}')
    logging.info('Ingestion Complete')

if __name__ == '__main__':
    logging.basicConfig(
    filename = "logs/ingestion_db.log",
    level=logging.DEBUG,
    format = "%(asctime)s-%(levelname)s-%(message)s",
    filemode = "a"
    )
    load_raw_data()