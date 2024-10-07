from urllib import response
import requests
from datetime import datetime

USERNAME="rberberi1"
TOKEN="abcdefghi65jklmnop"

pixela_endpoint="https://pixe.la/v1/users"

user_params={
  "token":TOKEN,
  "username":USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes",

}

# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
  "id": "graph0",
  "name": "Cycling Graph",
  "unit": "Km",
  "type": "float",
  "color" : "ajisai",
}

headers={
  "x-USER-TOKEN": TOKEN,
}

# response=requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph0"

today=datetime.now()

pixel_data={
  "date": today.strftime("%Y%m%d"),
  "quantity": "9.74",
}

# response=requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)
update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph0/{today.strftime('%Y%m%d')}"

new_pixel_data={
  "quantity": "20.3"
}

# response=requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/graph0/{today.strftime('%Y%m%d')}"

response=requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
