import requests

response = requests.get("http://api.open-notify.org/astros.json")

json = response.json();

print("People Currently in Space are: ")
for person in json["people"]:
    print(person["name"])
