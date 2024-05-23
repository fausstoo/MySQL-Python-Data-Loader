# MySQL Data Loader Pipeline with SQLAlchemy

## Overview

This project involves setting up a data loading pipeline that reads data from pickle files and loads it into a MySQL database using SQLAlchemy. The project is structured to follow best practices in software engineering, including modularization, the use of classes and objects, and proper error handling with logging.

## Project Structure

Booking_Data_Pipeline/ \
│ \
├── src/ \
│ ├── database.py \
│ ├── data_loader.py \
│ ├── exception.py \
│ ├── logger.py \
│ └── main.py \
│ \
├── data/ (contains .pkl files) \
│ \
├── logs/ (contains log files) \
│ \
├── requirements.txt \
│ \
└── README.md 

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd booking-pipeline
    ```

2. **Create a Conda environment**:
    ```bash
    conda create --name myenv python=3.11
    conda activate myenv
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure MySQL**:
    Ensure your MySQL is running and accessible. Add your credentials in `database.py`.

5. **Run the data loading script**:
    ```bash
    python src/data_loader.py
    ```

## Logging

Log files are generated in the `logs` directory, with detailed information about the data loading process, including any errors encountered.

## Error Handling

Custom exceptions are used to provide detailed error messages, facilitating easier debugging and maintenance.
