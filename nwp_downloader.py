import os
import yagmail
from credentials import Credentials, JsonFileBackend

from openweather_extract import OpenWeatherDownloader

path_nwp = '.'
file_cred = 'filemail.json'

credobj = Credentials([JsonFileBackend(file_cred)])


def send_predictions(date, filename):
    contents = ' '
    # The mail addresses and password
    sender_address = credobj.load('cred1')
    sender_pass = credobj.load('cred2')
    yag_smtp_connection = yagmail.SMTP(user=sender_address, password=sender_pass, host='smtp.gmail.com', smtp_ssl=False)

    subject = 'Openweather predictions for Athens for ' + date.strftime('%Y%m%d')
    receivers = ['joesider@power.ece.ntua.gr', 'supply@fysikoaerioellados.gr']
    for receiver_address in receivers:
        yag_smtp_connection.send(to=receiver_address, subject=subject, contents=contents,
                                 attachments=[filename])

    print('Mail Sent for Openweather predictions')


def NwpDownloader():
    open_weather_extractor = OpenWeatherDownloader(path_nwp)
    open_weather_extractor.download()
    send_predictions(open_weather_extractor.date, open_weather_extractor.filename)


if __name__ == '__main__':
    NwpDownloader()
