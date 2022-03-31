from email import header
import requests
import json
import secrets

url = "https://api.notion.com/v1/databases/{}/query".format(secrets.database)
payload = "{\"filter\": {\"or\": [ {\"property\": \"Semester\", \"multi_select\": {\"contains\": \"2\"} }, {\"property\": \"Semester\", \"multi_select\": { \"contains\": \"2\" }}]}}"
headers = {"Authorization": "Bearer {}".format(secrets.secret_key), "Content-Type": "application/json", "Notion-Version": "2022-02-22", 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=payload, headers=headers)

x = ((str(r.content))) #, ensure_ascii = False, indent=4))

x = json.loads(json.dumps(('{' + x[19:-1]).replace('\\', '')))

# print(x, file=open("output.json", 'w'))

# print(json.loads(x)["results"][1]["properties"]["Name"]["title"][0]["text"]["content"])

y = json.loads(x)["results"]

assignments = {}

for i in y:
    status = int(i["properties"]["Status"]["select"]["id"])

    if status == 1:
        assignments[i["properties"]["Name"]["title"][0]["text"]["content"]] = "To Do"
    elif status == 2:
        assignments[i["properties"]["Name"]["title"][0]["text"]["content"]] = "Doing"
    elif status == 3:
        assignments[i["properties"]["Name"]["title"][0]["text"]["content"]] = "Done"


print(assignments)