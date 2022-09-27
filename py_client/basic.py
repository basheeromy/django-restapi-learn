from urllib import request
import requests

endpoint = "http://localhost:8000/api/"
#endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint,params={"white":"black"},json={"product_id": 123 })
print(get_response.status_code)
print(get_response.json())
#print(get_response.text)
#print(get_response.headers)