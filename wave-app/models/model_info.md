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
