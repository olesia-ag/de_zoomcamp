-- to count number of trips on 2019-09-18
select count(*) from green_taxi_data where to_date(lpep_dropoff_datetime, 'YYYY-MM-DD HH24:MI:SS') < to_date('2019-09-19', 'YYYY-MM-DD HH:MI:SS')
and TO_date(lpep_pickup_datetime, 'YYYY-MM-DD HH24:MI:SS') >= to_date('2019-09-18', 'YYYY-MM-DD HH24:MI:SS')

-- largest trip for the day

select
CAST(lpep_pickup_datetime as DATE) as "day",
MAX(trip_distance)
from green_taxi_data
group by CAST(lpep_pickup_datetime as DATE)
order by max desc

-- check total sum in boroughs

select
CAST(lpep_pickup_datetime as DATE) as "day",
SUM(total_amount) as total,
zpu."Borough"
from
green_taxi_data t
JOIN
green_zones zpu ON
t."PULocationID" = zpu."LocationID" JOIN green_zones zdo ON
t."DOLocationID" = zdo."LocationID"
group by CAST(lpep_pickup_datetime as DATE), zpu."Borough"
order by total desc

-- largest tip in September from Astoria:
select
CAST(lpep_pickup_datetime as DATE) as "day",
MAX(tip_amount) as tip,
zpu."Zone",
zdo."Zone",
t.lpep_pickup_datetime
from
green_taxi_data t
JOIN
green_zones zpu ON
t."PULocationID" = zpu."LocationID" JOIN green_zones zdo ON
t."DOLocationID" = zdo."LocationID"
group by CAST(lpep_pickup_datetime as DATE), zpu."Zone", zdo."Zone", t.lpep_pickup_datetime
HAVING
 zpu."Zone" = 'Astoria'
order by tip desc
