import requests
url = 'http://127.0.0.1:5000/recipe'
##response = Forum.post(url,data={"name":"recipe", "expires_in": 30, "snippet":"1 apple"})
##response = requests.get(url)
myobj= {"name":"recipe", "expires_in": 30, "snippet":"1 apple"}
response = requests.post(url,data=myobj)
print(response.text)