import requests
url = 'http://172.28.0.2/results'
#r=requests.get("http://172.28.0.2/")
r = requests.post(url,json={'week':5, 'checkout_price':200, 'base_price':400})
#r=requests.post(url)


print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)

print(r.text)

