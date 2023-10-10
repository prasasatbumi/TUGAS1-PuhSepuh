# import library
import requests, json
from bs4 import BeautifulSoup

pages = [
    "https://forecast.weather.gov/MapClick.php?x=60&y=219&site=phi&zmx=&zmy=&map_x=60&map_y=218",
    "https://forecast.weather.gov/MapClick.php?x=155&y=202&site=okx&zmx=&zmy=&map_x=155&map_y=202",
    "https://forecast.weather.gov/MapClick.php?x=77&y=61&site=ffc&zmx=&zmy=&map_x=77&map_y=61"
    ]

data = {}

for i in pages:
  # request page
  page = requests.get(i)
  soup = BeautifulSoup(page.content, 'html.parser')
  seven_day = soup.find(id="seven-day-forecast")

  # place
  key = soup.select("h2.panel-title")[0].get_text()

  # desc
  day = seven_day.select(".tombstone-container img")
  descs = [d["title"] for d in day]
  desc=[]
  for i in descs:
    index = i.find(":")
    desc.append(i[(index+2):-2])

  # periods
  period_tags = seven_day.select(".tombstone-container .period-name")
  periods = [pt.get_text() for pt in period_tags]

  # make value from periods:desc
  value = {}
  for i in range(len(periods)):
    value[periods[i]]=desc[i]

  # insert to data place:value
  data[key]=value

# Serializing json
json_object = json.dumps(data, indent = 1,separators=(',', ':'))
print(json_object)

# Create file json
with open("data.json", "w") as outfile:
    outfile.write(json_object)