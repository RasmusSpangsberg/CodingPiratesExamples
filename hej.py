# importing the requests library
import requests
​
# api-endpoint
URL = "https://api.openweathermap.org/data/2.5/weather"
​
# location given here
location = "copenhagen"
​
# defining a params dict for the parameters to be sent to the API
PARAMS = {
    "q": location,
    "units": "metric",
    "appid": "3d1ce6db32676beec1a9647a3f7729c9"
}
​
# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)
​
# extracting data in json format
data = r.json()
​
print(data)