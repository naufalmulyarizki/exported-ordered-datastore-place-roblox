import requests
import json

API_KEY     = ""
UNIVERSE_ID = ""
STORE_NAME  = ""
SCOPE       = ""

url = f"https://apis.roblox.com/ordered-data-stores/v1/universes/{UNIVERSE_ID}/orderedDataStores/{STORE_NAME}/scopes/{SCOPE}/entries"

headers = {"x-api-key": API_KEY}
params  = {"max_page_size": 100, "order_by": "desc"}

exported = []

while True:
    response = requests.get(url, headers=headers, params=params)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")  # debug mentah
    
    data = response.json()
    entries = data.get("entries", [])
    
    for entry in entries:
        exported.append({"key": entry["id"], "value": entry["value"]})
        print(f"[EXPORT] key={entry['id']} | value={entry['value']}")
    
    next_token = data.get("nextPageToken")
    if not next_token:
        break
    params["page_token"] = next_token

with open("donortotals_export.json", "w") as f:
    json.dump(exported, f, indent=2)

print(f"\n[DONE] {len(exported)} entries")