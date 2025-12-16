# KYC API Call Guide

This guide provides instructions on how to call the KYC (Know Your Customer) API for user verification.

## API Endpoint

**POST** `http://nonabstemiously-stocky-cynthia.ngrok-free.dev/api/v1/user/initiate-verification/`

## Headers

The following headers are required for the API call:

| Header | Value | Description |
|--------|-------|-------------|
| `X-API-KEY` | Your secret key | Your API authentication key |
| `Content-Type` | `application/json` | Specifies that the request body is in JSON format |

## Example Request

### Using cURL

```bash
curl -X POST \
  http://nonabstemiously-stocky-cynthia.ngrok-free.dev/api/v1/user/initiate-verification/ \
  -H "X-API-KEY: your_secret_key_here" \
  -H "Content-Type: application/json" \
  -d '{
    "user_data": "your_data_here"
  }'
```

### Using Python (requests library)

```python
import requests
import json

url = "http://nonabstemiously-stocky-cynthia.ngrok-free.dev/api/v1/user/initiate-verification/"

headers = {
    "X-API-KEY": "your_secret_key_here",
    "Content-Type": "application/json"
}

data = {
    "user_data": "your_data_here"
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.json())
```

### Using JavaScript (Fetch API)

```javascript
const url = "http://nonabstemiously-stocky-cynthia.ngrok-free.dev/api/v1/user/initiate-verification/";

const headers = {
    "X-API-KEY": "your_secret_key_here",
    "Content-Type": "application/json"
};

const data = {
    user_data: "your_data_here"
};

fetch(url, {
    method: "POST",
    headers: headers,
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error("Error:", error));
```

### Using Node.js (axios)

```javascript
const axios = require('axios');

const url = "http://nonabstemiously-stocky-cynthia.ngrok-free.dev/api/v1/user/initiate-verification/";

const headers = {
    "X-API-KEY": "your_secret_key_here",
    "Content-Type": "application/json"
};

const data = {
    user_data: "your_data_here"
};

axios.post(url, data, { headers: headers })
    .then(response => {
        console.log(response.status);
        console.log(response.data);
    })
    .catch(error => {
        console.error("Error:", error);
    });
```

## Important Notes

- Replace `your_secret_key_here` with your actual API key
- Replace the request body (`user_data`) with the actual data required by the API
- Make sure to keep your API key secure and never commit it to version control
- The endpoint is using ngrok, which provides temporary URLs. The domain may change over time

## Response

The API will return a JSON response with the verification status and details.