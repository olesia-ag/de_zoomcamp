import io
import pandas as pd
import requests
import glob
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
    
    path = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-'
    
    main_df = pd.DataFrame()
    

    for i in range(10,13):
        url = path+str(i)+'.csv.gz'
        df = pd.read_csv(url, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)
        main_df=pd.concat([main_df, df])

    return main_df
    # return pd.read_csv(csv_files, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
