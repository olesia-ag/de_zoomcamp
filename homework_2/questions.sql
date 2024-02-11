-- Q1
-- 266855 rows x 20 columns


-- Q2
SELECT * FROM mage.green_taxi;
-- result: 139370 rows x 20 columns answer 4

--Q3
  -- data['lpep_pickup_datetime'] = data['lpep_pickup_date'].dt.date

-- Q4
SELECT DISTINCT(vendor_id) FROM mage.green_taxi;
-- answer: 1 or 2

-- Q5
print(data.dtypes)
-- answer: 4

-- Q6
-- answer: 96
