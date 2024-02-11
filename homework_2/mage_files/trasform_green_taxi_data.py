import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    # Treat missing values as 0
    data['passenger_count'] = data['passenger_count'].fillna(0)
    # lowercase and snake_case tranformation
    data.columns = (data.columns
                    .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                    .str.lower()
    )
    data.rename(columns={'lpep_pickup_datetime': 'lpep_pickup_date'}, inplace=True)
    data['lpep_pickup_date'] = data['lpep_pickup_date'].dt.date
    print(data.dtypes)
    # only return where passenger count and trip distance is not 0
    filtered_data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
    return filtered_data

    # return data[data['passenger_count'] > 0 & data['trip_distance'] > 0]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    # if 'passenger_count' in output.columns and 'trip_distance' in output.columns:
        # Check that there are no rows where passenger_count is not greater than 0
    assert('vendor_id' in output.columns), 'vendor_id is missing'
    assert (output['passenger_count'] > 0).all(), 'Some rows have passenger_count <= 0'
        # Check that there are no rows where trip_distance is not greater than 0
    assert (output['trip_distance'] > 0).all(), 'Some rows have trip_distance <= 0'