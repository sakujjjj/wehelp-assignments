import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    # data = response.read().decode("utf-8")
    data = json.load(response)
# print(data)
clist=data["result"]["results"]
with open("data.csv","w", encoding="utf-8") as file:
    for title in clist:
        file.write(title["stitle"]+","+title["address"][5:8]+","+title["longitude"]+","+title["latitude"]+","+title["file"].split("https://")[1]+"\n")

# for title in clist:
    # print(title["stitle"],title["address"][5:8],title["longitude"],title["latitude"],title["file"].split("https://")[1])

# ["stitle"]
# print(clist)