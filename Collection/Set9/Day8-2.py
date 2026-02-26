import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import json

URI="https://petstore3.swagger.io/api/v3/pet/findByStatus?status=available"

retry = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET", "PUT", "DELETE", "OPTIONS"],
    respect_retry_after_header=True
)

session = requests.Session()
session.mount("https://", HTTPAdapter(max_retries=retry))

response = session.get(URI, timeout=5)

print(json.dumps((response.json())[1], indent=2))
