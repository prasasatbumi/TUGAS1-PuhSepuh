# TUGAS1-PuhSepuh
**Project Description**

## Getting Started
This guide shows you how to use NoSQL container in docker and running a crawler application created to obtain semi-structured data on The National Weather Service (NWS) website.

### System Requirement
- Windows 10 64bit: Pro, Enterprise or Education (1607 Anniversary Update, Build 14393 or later).
- Virtualization is enabled in BIOS. Typically, virtualization is enabled by default. This is different from having Hyper-V enabled. For more detail see Virtualization must be enabled in Troubleshooting.
- CPU SLAT-capable feature.
- At least 4GB of RAM.

### Prerequisites
You need `Mongodb` distributed via `Docker` image. To download Docker Desktop for Windows, head to Docker Hub.

Link: https://hub.docker.com/editions/community/docker-ce-desktop-windows

After successful installation, you can do the following steps:

- To start a mongo server instance, run the following command:
```
docker run --name some-mongo -d mongo:latest
```
where some-mongo is the name you want to assign to your container.

- To get a bash shell inside your `mongo` container, run the following command:
```
docker exec -it some-mongo bash
```
- To connect to a MongoDB deployment running on localhost with default port 27017, run the following command:
```
mongosh
```

## Running the tests

First, you need a The National Weather Service (NWS) website link and put it in the `pages` list in the `main.py` file. For example:
```
pages = [
    "https://forecast.weather.gov/MapClick.php?x=60&y=219&site=phi&zmx=&zmy=&map_x=60&map_y=218",
    "https://forecast.weather.gov/MapClick.php?x=155&y=202&site=okx&zmx=&zmy=&map_x=155&map_y=202",
    "https://forecast.weather.gov/MapClick.php?x=77&y=61&site=ffc&zmx=&zmy=&map_x=77&map_y=61"
    ]
```
the example contains three links with various cities.
