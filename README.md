# TUGAS1-PuhSepuh
This project focuses on developing a comprehensive guide for dockworkers on setting up and utilizing a MongoDB container, an essential component of modern data management, and implementing a web scraping application to collect semi-structured data from the National Weather Service (NWS) website. The goal is to facilitate efficient data storage and retrieval processes while extracting valuable weather-related information.

## Getting Started
This guide shows you how to use Mongodb container in docker and running a crawler application created to obtain semi-structured data on The National Weather Service (NWS) website.

### System Requirement
- Windows 10 64bit: Pro, Enterprise or Education (1607 Anniversary Update, Build 14393 or later).
- Virtualization is enabled in BIOS. Typically, virtualization is enabled by default. This is different from having Hyper-V enabled. For more detail see Virtualization must be enabled in Troubleshooting.
- CPU SLAT-capable feature.
- At least 4GB of RAM.

### Prerequisites
You need `Mongodb` distributed via `Docker` image. To download Docker Desktop for Windows, head to Docker Hub.

Link: https://hub.docker.com/editions/community/docker-ce-desktop-windows

After successful installation, run `docker` application and do the following steps in `Command Prompt`:

- To start a mongo server instance, run the following command:
```
docker run --name some-mongo -d mongo:latest
```
where `some-mongo` is the name you want to assign to your container.

- To get a bash shell inside your `mongodb` container, run the following command:
```
docker exec -it some-mongo bash
```
- To connect to a mongodb deployment running on localhost with default port 27017, run the following command:
```
mongosh
```
- Create a new database. For example, the following commands create both the database `myNewDatabase` and the collection `myCollection`
```
use myNewDatabase
db.createCollection("myCollection")
```

## Running the tests

First, you need a The National Weather Service (NWS) website link and put it in the `pages` list in the `main.py` file. For example:
```
pages = [
    "https://forecast.weather.gov/MapClick.php?x=60&y=219&site=phi&zmx=&zmy=&map_x=60&map_y=218",
    "https://forecast.weather.gov/MapClick.php?x=155&y=202&site=okx&zmx=&zmy=&map_x=155&map_y=202"
    ]
```
The example contains two links with various cities. Then run the `main.py` file

After running, the `data.json` containing data from the The National Weather Service (NWS) website will appear. This is an example:
```
[
 {
  "Washington/Reagan National Airport, DC (KDCA)":{
   "Overnight":"Partly cloudy, with a low around 51. Calm wind",
   "Friday":"Sunny, with a high near 70. Northeast wind around 7 mph",
   "FridayNight":"Mostly clear, with a low around 51. Light northeast wind",
   "Saturday":"Showers, with thunderstorms also possible after 5pm.  High near 63. Southeast wind 5 to 9 mph.  Chance of precipitation is 80%. New rainfall amounts between a tenth and quarter of an inch, except higher amounts possible in thunderstorms",
   "SaturdayNight":"Showers and possibly a thunderstorm.  Low around 50. North wind 6 to 8 mph.  Chance of precipitation is 90",
   "Sunday":"Showers likely, mainly before 8am.  Mostly cloudy, with a high near 60. Chance of precipitation is 60",
   "SundayNight":"Mostly cloudy, with a low around 4",
   "Monday":"Partly sunny, with a high near 5",
   "MondayNight":"A chance of showers after 2am.  Mostly cloudy, with a low around 48. Chance of precipitation is 30"
  }
 },
 {
  "Farmingdale - Republic Airport (KFRG)":{
   "Overnight":"Clear, with a steady temperature around 52. North wind around 8 mph",
   "Friday":"Sunny, with a high near 65. Northwest wind 8 to 10 mph",
   "FridayNight":"Increasing clouds, with a low around 48. North wind around 6 mph",
   "Saturday":"Rain likely, mainly after 2pm.  Mostly cloudy, with a high near 60. Northwest wind 5 to 7 mph.  Chance of precipitation is 60%. New precipitation amounts between a quarter and half of an inch possible",
   "SaturdayNight":"Rain likely.  Cloudy, with a low around 49. Northeast wind 7 to 11 mph.  Chance of precipitation is 70%. New precipitation amounts between a half and three quarters of an inch possible",
   "Sunday":"A 30 percent chance of rain before 2pm.  Mostly cloudy, with a high near 6",
   "SundayNight":"Mostly cloudy, with a low around 5",
   "Monday":"Mostly cloudy, with a high near 6",
   "MondayNight":"A 30 percent chance of rain.  Mostly cloudy, with a low around 5"
  }
 }
]
```

Back to mongodb container running in `Command Prompt`, insert multiple document from `data.json` into a collection in database. For example:
```
use myNewDatabase
db.myCollection.insertMany([
   {
      "Washington/Reagan National Airport, DC (KDCA)":{
          "Overnight":"Mostly cloudy, with a low around 47. Calm wind",
          "Thursday":"Mostly sunny, with a high near 74. Calm wind becoming southwest around 6 mph in the afternoon",
          "ThursdayNight":"Partly cloudy, with a low around 53. East wind around 5 mph becoming calm  in the evening",
          "Friday":"Mostly sunny, with a high near 71. North wind around 7 mph",
          "FridayNight":"A chance of showers after 2am.  Partly cloudy, with a low around 54. East wind 3 to 6 mph.  Chance of precipitation is 40",
          "Saturday":"Showers likely, then showers and possibly a thunderstorm after 2pm.  High near 65. Chance of precipitation is 90",
          "SaturdayNight":"Showers and possibly a thunderstorm before 2am, then a chance of showers.  Low around 52. Chance of precipitation is 80",
          "Sunday":"A chance of showers before 2pm.  Mostly cloudy, with a high near 59. Chance of precipitation is 30",
          "SundayNight":"Mostly cloudy, with a low around 4"}
    },
    {
      "Farmingdale - Republic Airport (KFRG)":{
          "Overnight":"Patchy fog between 3am and 5am.  Otherwise, mostly clear, with a steady temperature around 52. North wind around 6 mph",
          "Thursday":"Patchy fog before 8am.  Otherwise, mostly sunny, with a high near 69. Calm wind becoming south around 6 mph in the afternoon",
          "ThursdayNight":"Partly cloudy, with a low around 51. Calm wind becoming north 5 to 7 mph after midnight",
          "Friday":"Sunny, with a high near 63. Northwest wind around 10 mph",
          "FridayNight":"Partly cloudy, with a low around 51. North wind around 7 mph",
          "Saturday":"Showers likely, mainly after 2pm.  Mostly cloudy, with a high near 58. Chance of precipitation is 70%. New precipitation amounts between a quarter and half of an inch possible",
          "SaturdayNight":"Showers likely.  Cloudy, with a low around 51. Chance of precipitation is 60",
          "Sunday":"A 40 percent chance of showers.  Mostly cloudy, with a high near 6",
          "SundayNight":"Mostly cloudy, with a low around 5"}
    }
])
```
After successfully entering data, mongodb will automatically add the `_id` field with an ObjectId value to each document.

To read all documents in the collection, pass an empty document as the query filter parameter to the find method. The query filter parameter determines the select criteria. For example:
```
use myNewDatabase
db.myCollection.find()
[
  {
    _id: ObjectId("6528e4c7b33e2442d817cea1"),
    'Washington/Reagan National Airport, DC (KDCA)': {
      Overnight: 'Partly cloudy, with a low around 51. Calm wind',
      Friday: 'Sunny, with a high near 70. Northeast wind around 7 mph',
      FridayNight: 'Mostly clear, with a low around 51. Light northeast wind',
      Saturday: 'Showers, with thunderstorms also possible after 5pm.  High near 63. Southeast wind 5 to 9 mph.  Chance of precipitation is 80%. New rainfall amounts between a tenth and quarter of an inch, except higher amounts possible in thunderstorms',
      SaturdayNight: 'Showers and possibly a thunderstorm.  Low around 50. North wind 6 to 8 mph.  Chance of precipitation is 90',
      Sunday: 'Showers likely, mainly before 8am.  Mostly cloudy, with a high near 60. Chance of precipitation is 60',
      SundayNight: 'Mostly cloudy, with a low around 4',
      Monday: 'Partly sunny, with a high near 5',
      MondayNight: 'A chance of showers after 2am.  Mostly cloudy, with a low around 48. Chance of precipitation is 30'
    }
  },
  {
    _id: ObjectId("6528e4c7b33e2442d817cea2"),
    'Farmingdale - Republic Airport (KFRG)': {
      Overnight: 'Clear, with a steady temperature around 52. North wind around 8 mph',
      Friday: 'Sunny, with a high near 65. Northwest wind 8 to 10 mph',
      FridayNight: 'Increasing clouds, with a low around 48. North wind around 6 mph',
      Saturday: 'Rain likely, mainly after 2pm.  Mostly cloudy, with a high near 60. Northwest wind 5 to 7 mph.  Chance of precipitation is 60%. New precipitation amounts between a quarter and half of an inch possible',
      SaturdayNight: 'Rain likely.  Cloudy, with a low around 49. Northeast wind 7 to 11 mph.  Chance of precipitation is 70%. New precipitation amounts between a half and three quarters of an inch possible',
      Sunday: 'A 30 percent chance of rain before 2pm.  Mostly cloudy, with a high near 6',
      SundayNight: 'Mostly cloudy, with a low around 5',
      Monday: 'Mostly cloudy, with a high near 6',
      MondayNight: 'A 30 percent chance of rain.  Mostly cloudy, with a low around 5'
    }
  }
]
```

To delete one documents in the collection, pass an empty document as the query filter parameter to the find method. The query filter parameter determines the select criteria. For example:
```
use yourDatabaseName
db.yourCollectionName.deleteOne({ _id: ObjectId("6528e4c7b33e2442d817cea2") });
```

then, the the result is :
```
{ acknowledged: true, deletedCount: 1 }
```
If that command pop out, then the data is successfully deleted. you can confirm it with command find()


Remember to replace yourDatabaseName, yourCollectionName, and the specific _id value as needed for your use case. Be cautious when deleting data, especially in a production environment, as there is no easy way to recover deleted documents. Always ensure you have proper backups or data retention policies in place.
