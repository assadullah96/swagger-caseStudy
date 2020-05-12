'''import requests

#resp = requests.get('http://petstore.swagger.io/?q=pet')
resp=requests.get('https://petstore.swagger.io')
print(resp.text)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /pet/ {}'.format(resp.status_code))
#for todo_item in resp.json():
    print('{} {}'.format(todo_item))
    '''
''' 
from urllib.request import urlretrieve
from urllib.parse import quote
qstr = quote("Stanford University")
thing = urlretrieve("https://www.duckduckgo.com/?q=" + qstr)
print(thing)
import requests
url_endpoint = 'https://www.duckduckgo.com'
mydict = {'q': 'whee! Stanford!!!', 'something': 'else'}
resp = requests.get(url_endpoint, params=mydict).json()
print(resp)'''

# importing the requests and json libraries
import requests, json
 
# defining the api key and endpoint
api_endpoint = 'http://petstore.swagger.io/v2/'

# put together the query parameters
data = json.dumps({'filters':["pet"], 'size':1})

# make the request
r = requests.post(url = api_endpoint, data = data)
 
# extracting response text 
response = r.text
print(response)