import requests

r = requests.get('https://api.github.com/events')

p = requests.post('http://httpbin.org/post', data={'key': 'value'})

pt = requests.put('http://httpbin.org/put', data={'key': 'value'})
d = requests.delete('http://httpbin.org/delete')
h = requests.head('http://httpbin.org/get')
o = requests.options('http://httpbin.org/get')

print(d, h, o)

