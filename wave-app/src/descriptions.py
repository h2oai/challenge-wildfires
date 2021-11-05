FIRMS_INFO = '''
### NASA FIRMS - Fire Information for Resource Management System
FIRMS distributes Near Real-Time (NRT) active fire data within 3 hours of satellite observation from the Moderate Resolution Imaging Spectroradiometer ([MODIS](https://modis.gsfc.nasa.gov/)) aboard the Aqua and Terra satellites, and the Visible Infrared Imaging Radiometer Suite ([VIIRS](https://www.jpss.noaa.gov/viirs.html)) aboard S-NPP and NOAA 20.

The raw archive fire/hotspot datasets could be requested at 
https://firms.modaps.eosdis.nasa.gov/download/ in yearly chunks for each instrument.
* MODIS Collection 6.1: Temporal Coverage: 11 November 2000 - present
* VIIRS S-NPP 375m: Temporal Coverage: 20 January 2012 - present
* VIIRS NOAA-20 375m: Temporal Coverage: 1 January 2020 - present

For all the data preparation steps please check our [Notebook](https://github.com/h2oai/challenge-wildfires/blob/main/notebook/DataPreparation.ipynb).
'''

BUSHFIRE_INFO = '''
### 2019–20 Australian bushfire season
From September 2019 until March 2020, when the final fire was extinguished, Australia had one of the worst bush fire seasons in its recorded history.
As it can be seen from the satellite dataset New South Wales and Victoria have been worst affected.
More than five million hectares, destroying more than 2,400 houses and forcing thousands to seek shelter elsewhere.
Source [wiki](https://en.wikipedia.org/wiki/2019%E2%80%9320_Australian_bushfire_season) [bbc](https://www.bbc.com/news/world-australia-50951043)
'''

ACKNOWLEDGEMENT = '''
### Acknowledgement & Disclaimer

We acknowledge the use of data and/or imagery from NASA's FIRMS (https://earthdata.nasa.gov/firms), part of NASA's Earth Observing System Data and Information System (EOSDIS).

* Do not use for the preservation of life or property. Satellite-derived active fire / thermal anomalies have limited accuracy.
* Active fire/thermal anomalies may be from fire, hot smoke, agriculture or other sources.
* Cloud cover may obscure active fire detections.

Please see the [official page](https://earthdata.nasa.gov/earth-observation-data/near-real-time/citation#ed-lance-disclaimer) for further details.
'''

MODEL_INFO = '''
### Modeling Approach
We zoomed in Australia and used aggressive aggregation for a simple baseline binary prediction model.

* Temporal resolution: Monthly
* Spatial resolution: 1 Decimal degree ~ 10 km grid
* Binary Target: At least two fire/hotspot detections

For each region we engineered a few simple features and trained a baseline lgb classification model.

To avoid leakage the following temporal splits were used for training.

* Training: 2014-2018
* Validation: 2019-2020
* Test: 2021

For all the details please check our offline training [Notebook](https://github.com/h2oai/challenge-wildfires/blob/main/notebook/AustraliaFirePrediction.ipynb).
'''
