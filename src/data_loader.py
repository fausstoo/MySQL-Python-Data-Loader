import os
import pandas as pd
from sqlalchemy import create_engine
from database import db_config 
from exception import CustomException
import logging
from logger import logging

class DataLoader:
    def __init__(self, db_config, data_folder):
        self.db_config = db_config
        self.data_folder = data_folder
        try:
            self.engine = create_engine(f"mysql+pymysql://{db_config.user}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.database}")
            logging.info("Database engine created successfully.")
        except Exception as e:
            logging.error(f"Failed to create database engine: {e}")
            raise CustomException(e, sys)

    def load_data(self):
        try:
            # Get all pickle files in the data folder
            pickle_files = [f for f in os.listdir(self.data_folder) if f.endswith('.pkl')]
            logging.info(f"Found pickle files: {pickle_files}")

            # Load each pickle file into a pandas DataFrame and write to MySQL
            for file in pickle_files:
                try:
                    table_name = os.path.splitext(file)[0]
                    df = pd.read_pickle(os.path.join(self.data_folder, file))
                    df.to_sql(name=table_name, con=self.engine, if_exists='replace', index=False)
                    logging.info(f"Loaded {table_name} into MySQL successfully.")
                except Exception as e:
                    logging.error(f"Failed to load {file} into MySQL: {e}")
                    raise CustomException(e, sys)
        except Exception as e:
            logging.error(f"Failed to load data: {e}")
            raise CustomException(e, sys)

def main():
    try:
        data_loader = DataLoader(db_config=db_config, data_folder='data')
        data_loader.load_data()
        logging.info("Data loading process completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
