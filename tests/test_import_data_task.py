import pytest
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../source'))
from source import importDataTask


@pytest.fixture
def fetch_data_api_response():
    url = "https://health.data.ny.gov/api/views/xdss-u53e/rows.json?accessType=DOWNLOAD"
    apiResponse = importDataTask.fetchDataFromApi(url)
    return apiResponse

def pytest_data_object():
    return {'data_object':None}

def pytest_column_list():
    return {'column_list':None}

def pytest_constructed_data_dictionary():
    return {'constructed_data_dictionary':None}

def test_fetch_data_api_response(fetch_data_api_response):
    assert ("data" in fetch_data_api_response and len(fetch_data_api_response["data"]) > 0)
    pytest.data_object = fetch_data_api_response["data"]


def test_get_all_columns_from_response(fetch_data_api_response):
    column_list = importDataTask.getAllColumnsFromResponse(fetch_data_api_response["meta"])
    if len(column_list) > 0:
        pytest.column_list = column_list
        assert True

def test_is_constructed_data_valid():
    actualColumnStartIndex = len(pytest.column_list) - 6
    constructed_data_dictionary  = importDataTask.constructRequiredDataDictionary(pytest.data_object, pytest.column_list, actualColumnStartIndex)
    if (len(constructed_data_dictionary["columns"]) > 0 and len(constructed_data_dictionary["data"]) > 0):
        pytest.constructed_data_dictionary = constructed_data_dictionary
        assert True

def test_county_object_mapping():
    countyObjectMapping = importDataTask.getCountyObjectMapping(pytest.constructed_data_dictionary)
    if len(countyObjectMapping) > 0:
        assert True
