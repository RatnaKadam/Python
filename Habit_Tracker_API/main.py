import requests
from datetime import datetime

TOKEN = "adbha23ajak34"
USERNAME = "ratna"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_header = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu",
}

# graph update
graph_update_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# get today's date
today = datetime.now()

# passing data into graph
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3.4"
}

response = requests.post(url=graph_update_endpoint, json=pixel_data, headers=graph_header)
