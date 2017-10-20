import os
from nose.tools import eq_
from pyexcel_xls import get_data


def test_hidden_row():
    data = get_data(os.path.join("tests", "fixtures", "hidden.xls"),
                    skip_hidden_row_and_column=True)
    expected = [[1, 3], [7, 9]]
    eq_(data['Sheet1'], expected)
