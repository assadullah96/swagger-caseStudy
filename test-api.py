
# importing the requests and json libraries
import requests, json

api_endpoint = 'http://petstore.swagger.io/v2/'

# put together the query parameters
data = json.dumps({'filters':["pet"], 'size':1})

# make the request
r = requests.post(url = api_endpoint, data = data)
 
# extracting response text 
response = r.text
print(response)