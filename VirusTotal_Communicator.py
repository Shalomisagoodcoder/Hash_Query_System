import json
import requests

def virustotal(MD5_Hash):
    #Ensure that there is no trailing spaces from the MD5_Hash value
    MD5_Hash = remove_trailing_spaces(MD5_Hash)

    url = f"https://www.virustotal.com/api/v3/files/{MD5_Hash}"

    headers = {
        "accept": "application/json",
        "x-apikey": "PLACE_YOUR_KEY_HERE"
    }

    response = requests.get(url, headers=headers)

    # Parse the JSON content
    data = json.loads(response.text)
    return data

def remove_trailing_spaces(input_string):
    # Use rstrip() to remove trailing spaces
    cleaned_string = input_string.rstrip()
    return cleaned_string

