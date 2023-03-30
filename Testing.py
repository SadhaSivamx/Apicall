
# import requests module
import requests
import json
# Making a get request
response = requests.get('https://d151-27-5-114-223.in.ngrok.io/')
  
for x in eval(response.content.decode()):
    print(x)