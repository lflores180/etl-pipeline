# ETL pipeline

## Introduction
This repository contains code from an ETL pipeline project I did in my bootcamp

- Extracts transactional data form a local database
- Identifies and removes duplicates
- Loads the transformed data to a s3 bucket

## Requirements
- The minimum requirement is Python3 
- Import the necessary libraries as [here](https://github.com/lflores180/etl-pipeline/blob/main/requirements.txt)

## Step by step:
1. Clone the repository, and change the directory to **etl-pipeline**:
```
git clone https://github.com/lflores180/etl-pipeline.git
```

- Please contact me for a copy of the database if you do not have it, otherwise update the [file path](https://github.com/lflores180/etl-pipeline/blob/e3c3492cfa53b855def6642a72bd906375359849/src/extract.py#L6) accordingly. 
- Create a .env file with connection passwords in your  **etl-pipeline** folder, similar to [this](https://github.com/lflores180/etl-pipeline/blob/e3c3492cfa53b855def6642a72bd906375359849/env.copy).
- To execute the code to extract, transform and load data to s3, run the `main.py` file:

Mac users:
```
python3 main.py
```

Window users:
```
python main.py
```
