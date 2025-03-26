import pandas as pd
from pytz import timezone


def convert_timezone(data, timezone1='Europe/Athens', timezone2='UTC'):
    def datetime_exists_in_tz(dt, tz):
        try:
            dt.tz_localize(tz)
            return True
        except:
            return False

    dates = data.index
    indices = [i for i, t in enumerate(dates) if datetime_exists_in_tz(t, tz=timezone(timezone1))]
    data = data.iloc[indices]
    dates = dates[indices]
    dates = dates.tz_localize(timezone(timezone1))
    dates = dates.tz_convert(timezone(timezone2))
    dates = [pd.to_datetime(dt.strftime('%d%m%y%H%M'), format='%d%m%y%H%M') for dt in dates]
    data.index = dates
    return data


def convert_timezone_dates(dates, timezone1='Europe/Athens', timezone2='UTC'):
    def datetime_exists_in_tz(dt, tz):
        try:
            dt.tz_localize(tz)
            return True
        except:
            return False

    indices = [i for i, t in enumerate(dates) if datetime_exists_in_tz(t, tz=timezone(timezone1))]
    dates = dates[indices]
    dates = dates.tz_localize(timezone(timezone1))
    dates = dates.tz_convert(timezone(timezone2))
    dates = [pd.to_datetime(dt.strftime('%d%m%y%H%M'), format='%d%m%y%H%M') for dt in dates]
    return dates

