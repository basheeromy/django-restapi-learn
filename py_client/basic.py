from urllib import request
import requests

endpoint = "http://127.0.0.1:8000/api/"
#endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint)
print(get_response.text)
print(get_response.json()['message'])