import requests, json

url = "https://webexapis.com/v1/memberships"
headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer MjljMGUzOTAtM2QxYi00OGUwLTg0MTctMWNiZTlkZWZjMzc0ZmZhOTQwODgtZjJl_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
}

lico = []
roomId = input('Room Id: ')

for e in lico:
    payload = {
    "roomId": roomId,
    "personEmail":e
    }
    response = requests.post(url, data = json.dumps(payload), headers=headers)

print("Done.")