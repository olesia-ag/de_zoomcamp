import io
import pandas as pd
import requests
import json
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    taxi_dtypes = {
        'VendorID':pd.Int64Dtype(),
        'passenger_count':pd.Int64Dtype(),
        'trip_distance':float,
        'RatecodeID':float,
        'store_and_fwd_flag':str,
        'PULocationID':pd.Int64Dtype(),
        'DOLocationID':pd.Int64Dtype(),
        'payment_type':pd.Int64Dtype(),
        'fare_amount':float,
        'extra':float,
        'mta_tax':float,
        'tip_amount':float,
        'tolls_amount':float,
        'improvement_surcharge':float,
        'total_amount':float,
        'congestion_surcharge':float
    }
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    
    path = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-'    
    main_df = pd.DataFrame()
    

    for i in range(1,13):
        if i < 10:
            url = path+'0'+str(i)+'.parquet'
        else: 
            url = path+str(i)+'.parquet' 
        df = pd.read_parquet(url, engine='auto', columns=taxi_dtypes)
        main_df=pd.concat([main_df, df])

    return main_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'