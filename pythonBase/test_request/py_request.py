import requests
from requests import exceptions






r = requests.get('http://127.0.0.1:8000/ip')
print(r.headers)
print()
print(r.json())
print(r.cookies)
print(r.url)
print(r.status_code)
print(r.content)
print(r.encoding)
print(r.is_redirect)
print(r.reason)
print(r.text)
print(r.apparent_encoding)
print(r.history)
print(r.raw)
