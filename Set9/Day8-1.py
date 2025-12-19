import requests
import json

URI="https://petstore3.swagger.io/api/v3"
URI1="https://petstore3.swagger.io/api/v3/user/logout"

statusType="available"

response1=requests.options(URI1)
print(response1.headers.get("Access-Control-Allow-Methods"))

response=requests.get(f"{URI}/pet/findByStatus", params={"status":statusType})
data=response.json()
print(f"Total pets are {len(data)}")
print(json.dumps(data[2], indent=2))

assert response.status_code == 200

tags=data[2].get("tags", [])
print(f"Tags type is List(True) or not(False) - {isinstance(tags, list)}")

assert any(
    tag.get("name") == "Russian Blue"
    for tag in data[2].get("tags", [])
)