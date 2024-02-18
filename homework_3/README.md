## creating external table from the bucket in BQ:

CREATE OR REPLACE EXTERNAL TABLE ny_taxi.taxi_green_2022_data
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://de_homework_3_olesia/green_taxi_data_2022.parquet']
)

##creating table in BQ:

CREATE OR REPLACE TABLE ny_taxi.taxi_green_2022_data_non_partitioned
AS SELECT vendor_id, passenger_count , TIMESTAMP_MICROS(CAST(lpep_pickup_datetime/1000 as INT64)) AS lpep_pickup_datetime,
TIMESTAMP_MICROS(CAST(lpep_dropoff_datetime/1000 as INT64)) AS lpep_dropoff_datetime, trip_distance , ratecode_id , store_and_fwd_flag , pulocation_id , dolocation_id , payment_type , fare_amount , extra , mta_tax , tip_amount , tolls_amount , improvement_surcharge , total_amount , congestion_surcharge
FROM `ny_taxi.taxi_green_2022_data`
WHERE
  lpep_pickup_datetime IS NOT NULL AND lpep_pickup_datetime > 0 AND
  lpep_dropoff_datetime IS NOT NULL AND lpep_dropoff_datetime > 0;

## Question 1
SELECT COUNT(*) FROM ny_taxi.taxi_green_2022_data_non_partitioned

## Question 2

SELECT COUNT(DISTINCT pulocation_id) FROM ny_taxi.taxi_green_2022_data
SELECT COUNT(DISTINCT pulocation_id) FROM ny_taxi.taxi_green_2022_data_non_partitioned

## Question 3
SELECT COUNT(*) FROM ny_taxi.taxi_green_2022_data
WHERE fare_amount = 0

## Question 4
CREATE OR REPLACE TABLE ny_taxi.taxi_green_2022_data_partitioned_clustered
PARTITION BY
DATE(lpep_pickup_datetime)
CLUSTER BY vendor_id AS
SELECT vendor_id, passenger_count , TIMESTAMP_MICROS(CAST(lpep_pickup_datetime/1000 as INT64)) AS lpep_pickup_datetime,
TIMESTAMP_MICROS(CAST(lpep_dropoff_datetime/1000 as INT64)) AS lpep_dropoff_datetime, trip_distance , ratecode_id , store_and_fwd_flag , pulocation_id , dolocation_id , payment_type , fare_amount , extra , mta_tax , tip_amount , tolls_amount , improvement_surcharge , total_amount , congestion_surcharge
FROM `ny_taxi.taxi_green_2022_data`
WHERE
  lpep_pickup_datetime IS NOT NULL AND lpep_pickup_datetime > 0 AND
  lpep_dropoff_datetime IS NOT NULL AND lpep_dropoff_datetime > 0;

## Question 5
SELECT pulocation_id FROM ny_taxi.taxi_green_2022_data_partitioned_clustered
WHERE DATE(lpep_pickup_datetime) between '2022-06-01' and '2022-06-30'

SELECT pulocation_id FROM ny_taxi.taxi_green_2022_data_non_partitioned
WHERE DATE(lpep_pickup_datetime) between '2022-06-01' and '2022-06-30'

Result: 12.82 and 1.12

