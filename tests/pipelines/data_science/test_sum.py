from spaceflights_pandas.pipelines.data_science.sum import sum_two_integers


def test_sum_two_integers():
    assert sum_two_integers(1, 2) == 3
    assert sum_two_integers(-1, 1) == 0
    assert sum_two_integers(0, 0) == 0
    assert sum_two_integers(-1, -1) == -2
    assert sum_two_integers(100, 200) == 300
