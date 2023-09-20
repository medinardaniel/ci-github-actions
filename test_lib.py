import pandas as pd
# append the path of the src directory to import the lib module
# sys.path.append('./')
from lib import get_mean_median_mode, bar_chart, get_percentiles

# Assuming your functions are in a module named "your_module_name"
# and df is a DataFrame with relevant data

def test_get_mean_median_mode():
    df = pd.DataFrame({'column': [1, 2, 3, 3, 4, 5, 5, 5]})
    mean_val, median_val, mode_val = get_mean_median_mode(df, 'column')

    assert mean_val == 3.5
    assert median_val == 3.5
    assert mode_val[0] == 5

def test_get_percentiles():
    df = pd.DataFrame({'column': [10, 20, 30, 40, 50]})
    percentile_25, percentile_50, percentile_75 = get_percentiles(df, 'column')

    assert percentile_25 == 20
    assert percentile_50 == 30
    assert percentile_75 == 40
