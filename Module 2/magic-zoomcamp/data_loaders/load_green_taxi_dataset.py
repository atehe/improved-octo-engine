import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    months = [10, 11, 12]
    year = 2020

    month_dfs = []

    for month in months:
        
        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{month}.csv.gz'
        df =  pd.read_csv(url, sep=',', compression='gzip', parse_dates=['lpep_pickup_datetime','lpep_dropoff_datetime'])

        print(f"Found {len(df)} records for {month}-{year}")
        month_dfs.append(df)


    return pd.concat(month_dfs)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
