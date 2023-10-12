# import library
import requests, json
from bs4 import BeautifulSoup


def crawl(pages):

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