# APIs: Application Programming Interfaces

## What is an API?

An API (Application Programming Interface) is a set of protocols and tools that allows different software applications to communicate with each other. It defines the methods and data structures that developers can use to interact with an external service or application.

In practical terms, an API enables your application to request and receive data from another system over the internet. For instance, a weather application retrieves meteorological data through a weather service API, which provides current conditions, forecasts, and historical weather information.

## How to Interact with an API

APIs are accessed through **endpoints** - specific URLs that correspond to different resources or actions within the service.

### Key Concepts

**Endpoint**: The URL that represents a specific API resource or function
- Example: `https://api.weather.com/v1/current`

**Payload**: The structured data sent to or received from the API, typically formatted as JSON
- Example: `{"location": "Toronto", "units": "metric", "celsius_reading": 30.5}`

## GET Requests: Retrieving Data

GET requests are used to **retrieve data** from an API without modifying any server-side resources. This is the most common type of API request.

**Example: Retrieving current weather data**
```bash
curl "https://api.weather.com/v1/current?location=Toronto&units=metric"
```

**Python example:**
```python
import requests

response = requests.get(
    "https://api.weather.com/v1/current",
    params={"location": "Toronto", "units": "metric"}
)
weather_data = response.json()
print(weather_data)
```

**Response example:**
```json
{
  "location": "Toronto",
  "temperature": 15,
  "conditions": "Partly Cloudy",
  "humidity": 65
}
```

**Process:**
- The client sends a GET request to the endpoint with query parameters
- The API processes the request and queries its data source
- The API returns the requested data in JSON format
- No modifications are made to server-side data

## POST Requests: Sending Data

POST requests are used to **send data** to an API, typically to create new resources or submit information for processing.

**Example: Submitting a weather observation**
```bash
curl -X POST https://api.weather.com/v1/observations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "location": "Toronto",
    "temperature": 16,
    "conditions": "Sunny",
    "timestamp": "2025-11-25T14:30:00Z"
  }'
```

**Python example:**
```python
import requests

payload = {
    "location": "Toronto",
    "temperature": 16,
    "conditions": "Sunny",
    "timestamp": "2025-11-25T14:30:00Z"
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.post(
    "https://api.weather.com/v1/observations",
    json=payload,
    headers=headers
)
result = response.json()
print(result)
```

**Response example:**
```json
{
  "status": "success",
  "observation_id": "obs_789456",
  "message": "Weather observation recorded successfully"
}
```

**Process:**
- The client sends a POST request with data in the request body
- The API receives and validates the payload
- The API processes the data (stores it, performs calculations, etc.)
- The API returns a response confirming the operation

## Summary

- **GET**: Retrieves data from an API endpoint without modifying server resources
- **POST**: Sends data to an API endpoint to create or process information
- **Endpoint**: The specific URL that represents an API resource or function
- **Payload**: The structured data exchanged between client and server, typically in JSON format