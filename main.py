import crawl

""" Insert link in the list """
pages = [
    "https://forecast.weather.gov/MapClick.php?x=60&y=219&site=phi&zmx=&zmy=&map_x=60&map_y=218",
    "https://forecast.weather.gov/MapClick.php?x=155&y=202&site=okx&zmx=&zmy=&map_x=155&map_y=202",
    "https://forecast.weather.gov/MapClick.php?x=77&y=61&site=ffc&zmx=&zmy=&map_x=77&map_y=61"
    ]

crawl.crawl(pages)