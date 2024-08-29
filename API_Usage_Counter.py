import requests
import json

def get_response():
    url = "https://www.virustotal.com/api/v3/users/PLACE_YOUR_KEY_HERE/overall_quotas"

    headers = {
        "accept": "application/json",
        "x-apikey": "PLACE_YOUR_KEY_HERE"
    }

    response = requests.get(url, headers=headers)

    return api_token_finder(response.text)

def api_token_finder(response):
    # Load the JSON data into a Python dictionary
    data = json.loads(response)

    # Navigate through the dictionary to get the 'used' value
    try:
        used_value = data['data']['api_requests_daily']['user']['used']
        return used_value
    except KeyError as e:
        print('\n' + '#' * 140)
        print(f"KeyError: {e} not found in the JSON data")
        print("\nHere is a possible reason for this error:")
        print("-You didn't add your API key in file API_Usage_Checker")
        print("\nPlease ensure that you have added your API key in both the url and headers variables")
        print('#' * 140)
        return None
