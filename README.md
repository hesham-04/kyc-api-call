# KYC API Call

Simple Python script to call the KYC (Know Your Customer) API for user verification. Just download and run the python file. It will return a URL that will contain the KYC flow for the UUID that was sent.
Only one Session/KYC flow will be generated against each UUID.

## Configuration


```python
BASE_URL = "http://nonabstemiously-stocky-cynthia.ngrok-free.dev"
ENDPOINT = "/api/v1/user/initiate-verification/"
API_KEY = "sk_test_0fb8OebMdTc8JNyk7HAWpNPTEm7YvMcDZgnfRTKistk"
USER_UUID = random.randint(1, 9999)
```

### User UUID

| Environment | Value | Example |
|-------------|-------|---------|
| **Test** | Random digit | `random.randint(1, 9999)` |
| **Production** | Actual UUID | `"550e8400-e29b-41d4-a716-446655440000"` |

In production, replace the random digit with your actual user UUID:

```python
# Production
USER_UUID = "550e8400-e29b-41d4-a716-446655440000"
```

## Usage

```bash
python kyc-python.py
```

## What it does

1. Sends a POST request to the KYC API endpoint
2. Includes API key in headers (`X-API-KEY`)
3. Sends `user_uuid` in the request body
4. Prints the HTTP status code and JSON response

## Output Example

```
HTTP 200
{
    "status": "success",
    "message": "Verification initiated",
    "data": {...}
}
```

## JavaScript Example

```javascript
const BASE_URL = "http://nonabstemiously-stocky-cynthia.ngrok-free.dev";
const ENDPOINT = "/api/v1/user/initiate-verification/";
const API_KEY = "sk_test_0fb8OebMdTc8JNyk7HAWpNPTEm7YvMcDZgnfRTKistk";
const USER_UUID = Math.floor(Math.random() * 9999) + 1;

fetch(`${BASE_URL}${ENDPOINT}`, {
    method: "POST",
    headers: {
        "X-API-KEY": API_KEY,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ user_uuid: USER_UUID })
})
.then(response => response.json())
.then(data => console.log(JSON.stringify(data, null, 4)))
.catch(error => console.error("Error:", error));
```
