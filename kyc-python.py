import json
import requests
import random

# -----------------------------
# CONFIG — change deliberately
# -----------------------------
BASE_URL = "http://nonabstemiously-stocky-cynthia.ngrok-free.dev"
ENDPOINT = "/api/v1/user/initiate-verification/"
API_KEY = "sk_test_0fb8OebMdTc8JNyk7HAWpNPTEm7YvMcDZgnfRTKistk"
USER_UUID = random.randint(1, 9999)

# -----------------------------
# REQUEST
# -----------------------------
url = f"{BASE_URL}{ENDPOINT}"

headers = {
    "X-API-KEY": API_KEY,
    "Content-Type": "application/json",
}

payload = {
    "user_uuid": USER_UUID
}

response = requests.post(
    url,
    headers=headers,
    json=payload,
    timeout=10
)

# -----------------------------
# OUTPUT
# -----------------------------
print(f"HTTP {response.status_code}")

try:
    data = response.json()
    print(json.dumps(data, indent=4))
except ValueError:
    print("Non-JSON response:")
    print(response.text)
