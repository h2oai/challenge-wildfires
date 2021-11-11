# H2O.ai Wildfire & Bushfire Challenge Dataset

Thanks to NASA's full and open sharing [Data Policy](https://science.nasa.gov/earth-science/earth-science-data/data-information-policy/) we acknowledge the use of data and/or imagery from NASA's FIRMS (https://earthdata.nasa.gov/firms), part of NASA's Earth Observing System Data and Information System (EOSDIS).

### Disclaimer
* Do not use for the preservation of life or property. Satellite-derived active fire / thermal anomalies have limited accuracy.
* Active fire/thermal anomalies may be from fire, hot smoke, agriculture or other sources.
* Cloud cover may obscure active fire detections.

Please see the [official page](https://earthdata.nasa.gov/earth-observation-data/near-real-time/citation#ed-lance-disclaimer) for further details.

### Reproducibility
The archive fire/hotspot datasets could be [requested in yearly chunks for each instrument](https://firms.modaps.eosdis.nasa.gov/download/).

* MODIS Collection 6.1: Temporal Coverage: 11 November 2000 - present
* VIIRS S-NPP 375m: Temporal Coverage: 20 January 2012 - present
* VIIRS NOAA-20 375m: Temporal Coverage: 1 January 2020 - present

Since NOAA-20 has less than 2 years data we collected the other instruments. 

Please check our [Wildfire Challenge Starter Kit](https://github.com/h2oai/challenge-wildfires) as an example how to use the provided datasets.

### Download
For easy access we uploaded eight years of raw sensor data to [S3](https://s3.us-west-1.amazonaws.com/ai.h2o.challenge.datasets/wildfire-challenge/firms_fires_2013_2021.zip). 
