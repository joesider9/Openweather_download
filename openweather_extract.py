import requests

import os
import datetime
import pandas as pd

from credentials import Credentials, JsonFileBackend

from utils import convert_timezone_dates



class OpenWeatherDownloader:

    def __init__(self, path_nwp, date=None):
        self.path_nwp = path_nwp
        if date is None:
            self.date = pd.to_datetime(datetime.datetime.now().strftime('%d%m%y'), format='%d%m%y')
        else:
            self.date = date
        self.dates = pd.date_range(self.date, self.date + pd.DateOffset(hours=48), freq='H')
        self.dates = pd.DatetimeIndex(convert_timezone_dates(self.dates))
        self.lat1, self.long1 = 38, 23.73
        fname = 'openweather_' + self.date.strftime('%d%m%y') + '.csv'
        self.filename = os.path.join(path_nwp, fname)

    def download(self):
        url1 = f'https://api.openweathermap.org/data/2.5/onecall?lat={self.lat1}&lon={self.long1}&exclude=daily,minutely' \
               f'current,alerts&units=metric'

        response1 = requests.get(url1)
        if response1.status_code == 200:
            try:
                nwp1 = response1.json()["hourly"]
            except:
                raise ValueError('Openweather nwps are not downloaded correctly')
        else:
            raise ConnectionError('Openweather is not respond')
        for nwp in nwp1:
            del nwp['weather']
        nwp1 = pd.DataFrame().from_dict(nwp1)
        nwp1.dt = pd.to_datetime(nwp1.dt, unit='s')
        nwp1 = nwp1.set_index('dt')
        nwp1.to_csv(self.filename)
