import requests

status = 'available'
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
data = {'name': 'smutov'}
data_change = {'name': 'NOTsmutov'}
base_url = f'https://petstore.swagger.io/v2/pet/'

res = requests.get(base_url + f'findByStatus?status={status}', headers=headers)

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

res = requests.post(base_url + '', headers=headers, json=data)

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

res = requests.put(base_url, json=data_change)

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

petid = 9223372036854775807
res = requests.delete(base_url + f'{petid}')

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))