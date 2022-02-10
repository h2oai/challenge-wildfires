import requests
import pandas as pd

url_7d = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Australia_NewZealand_7d.csv"
url_24hrs = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Australia_NewZealand_24h.csv"


def converter(text):
    resArr = text.split("\n")
    arr = []
    for i in resArr:
        arr.append(i.split(","))
    df = pd.DataFrame(arr[1:-1], columns=arr[0])
    return df


def modis7ds():
    response = requests.get(url_7d)
    return converter(response.text)


def modis24hrs():
    response = requests.get(url_7d)
    return converter(response.text)

