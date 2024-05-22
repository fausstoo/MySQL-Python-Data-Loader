from database import Database
from create_tables import TableCreator
from load_data import DataLoader
from pyspark.sql import SparkSession

def main():
    # Initialize database connection
    db = Database("localhost", "root", "123456Fa$$", "booking_data")
    db.connect()

    # Create tables
    table_creator = TableCreator(db)
    table_creator.create_tables()

    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("MySQL_PySpark_Pipeline") \
        .config("spark.jars", "/path/to/mysql-connector-java-8.0.33.jar") \
        .getOrCreate()

    # Load data
    data_loader = DataLoader(db, spark, 'data')
    data_loader.load_data()

    # Close connections
    db.close()
    spark.stop()

if __name__ == "__main__":
    main()
