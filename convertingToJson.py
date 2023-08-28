import json
import requests

API_URL = 'https://www.travel-advisory.info/api'

def fetch_data_from_api(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")
        return None

def save_data_to_json(data, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to {file_name}")

def main():
    api_data = fetch_data_from_api(API_URL)
    if api_data:
        save_data_to_json(api_data, 'data.json')

if __name__ == "__main__":
    main()
