import requests

BASE = " http://127.0.0.1:5000/"

data = [{"likes": 10, "name": "a", "views": 2000},
        {"likes": 120, "name": "b", "views": 200000},
        {"likes": 3000, "name": "c", "views": 4000}]

#to add data to the db
for i in range(len(data)):
  response = requests.put(BASE + "id/"+str(i),data[i])
	print(response.json())

#to delete a data from db
response = requests.delete(BASE + 'id/0')
print(response)

#to fetch a data from db
response = requests.get(BASE + "id/1")
print(response.json())

#to update data in db
response = requests.patch(BASE + "id/1", {"name": "d", "views": 200000, "likes": 120})
print(response.json())
