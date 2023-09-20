import pandas as pd
import pytest
# import sys
# sys.path.append('../')
from descriptive_stats import descriptive_stats, create_bar_charts

def test_descriptive_stats():
    df = pd.DataFrame({'age': [20, 25, 30, 35, 40]})

    results = descriptive_stats(df, 'age')

    assert results['mean'] == 30
    assert results['median'] == 30
    assert results['mode'][0] == 20
    assert results['25th_percentile'] == 25
    assert results['50th_percentile'] == 30
    assert results['75th_percentile'] == 35

