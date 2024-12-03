
import requests
import json
import pandas as pd

# Set up API request
BLS_API_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
API_KEY = "17bce7d6b41147c597fde4dddd66e58c"


series_ids = [
    "CEU0000000001",  
    "LRU00000000"      
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
def process_data(data):
    series_data = data["results"]["series"][0]["data"]
    df = pd.DataFrame(series_data)
    df["date"] = pd.to_datetime(df["year"] + df["period"], format='%YM%m')
    df["value"] = df["value"].astype(float)
    return df

processed_data = {}
for series_id, data in data.items():
    processed_data[series_id] = process_data(data)