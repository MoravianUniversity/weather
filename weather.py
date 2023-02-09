from bs4 import BeautifulSoup
import requests


def get_weather():
    contents = requests.get('http://forecast.weather.gov/MapClick.php?lat=40.6222&lon=-75.3932')
    soup = BeautifulSoup(contents.text, 'html.parser')

    forecasts = soup.find_all('img', class_='forecast-icon')

    weather = []
    for forecast in forecasts:
        weather.append(forecast['alt'])
    return weather


def output_weather(weather_list):
    for report in weather_list:
        print(report)

if __name__ == '__main__':
    weather = get_weather()
    output_weather(weather)

