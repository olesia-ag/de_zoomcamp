-- to count number of trips on 2019-09-18
select count(*) from green_taxi_data where to_date(lpep_dropoff_datetime, 'YYYY-MM-DD HH24:MI:SS') < to_date('2019-09-19', 'YYYY-MM-DD HH:MI:SS')
and TO_date(lpep_pickup_datetime, 'YYYY-MM-DD HH24:MI:SS') >= to_date('2019-09-18', 'YYYY-MM-DD HH24:MI:SS')

