import requests
import json

# STEP 1: Public REST API URL
url = "https://jsonplaceholder.typicode.com/users"

# STEP 2: Custom headers
headers = {
    "Accept": "application/json",
    "User-Agent": "Python-Requests-Training"
}

try:
    # STEP 3: Send GET request with headers
    response = requests.get(url, headers=headers)

    # STEP 4: Handle HTTP errors
    response.raise_for_status()

    # STEP 5: Parse JSON response
    users = response.json()

    # STEP 6: Extract specific fields
    extracted_data = []
    for user in users:
        extracted_data.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        })

    # STEP 7: Save extracted data into a JSON file
    with open("users_data.json", "w") as file:
        json.dump(extracted_data, file, indent=4)

    print("Data successfully fetched and saved to users_data.json")

# STEP 8: Exception handling
except requests.exceptions.HTTPError as http_err:
    print("HTTP error occurred:", http_err)

except requests.exceptions.RequestException as err:
    print("Request error occurred:", err)
