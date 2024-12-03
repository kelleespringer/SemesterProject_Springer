import requests
import json
import pandas as pd

BLS_API_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
API_KEY = "17bce7d6b41147c597fde4dddd66e58c"  # Replace with your API key

series_ids = [
    "CEU0000000001",  # Non-farm payroll employment
    "LRU00000000"      # Unemployment rate
]

def fetch_bls_data(series_id, start_year="2020", end_year="2024"):
    params = {
        "registrationKey": API_KEY,
        "startYear": start_year,
        "endYear": end_year,
        "seriesid": [series_id]
    }
    response = requests.get(BLS_API_URL, params=params)
    data = response.json()
    return data

def fetch_all_data():
    all_data = {}
    for series_id in series_ids:
        all_data[series_id] = fetch_bls_data(series_id)
    return all_data

def save_data(data, filename="data/bls_data.json"):
    with open(filename, 'w') as file:
        json.dump(data, file)

data = fetch_all_data()
save_data(data)