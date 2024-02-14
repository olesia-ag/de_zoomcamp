## creating external table from the bucket in BQ:

CREATE OR REPLACE EXTERNAL TABLE ny_taxi.taxi_green_2022_data
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://de_homework_3_olesia/green_taxi_data_2022.parquet']
)

##creating table in BQ:

CREATE OR REPLACE TABLE ny_taxi.taxi_green_2022_data_non_partitioned
AS SELECT * FROM `ny_taxi.taxi_green_2022_data`

## Question 1
SELECT COUNT(*) FROM ny_taxi.taxi_green_2022_data_non_partitioned

## Question 2

SELECT COUNT(DISTINCT pulocation_id) FROM ny_taxi.taxi_green_2022_data
SELECT COUNT(DISTINCT pulocation_id) FROM ny_taxi.taxi_green_2022_data_non_partitioned

## Question 3
SELECT COUNT(*) FROM ny_taxi.taxi_green_2022_data
WHERE fare_amount = 0

