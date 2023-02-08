from bs4 import BeautifulSoup
import requests

contents = requests.get('http://forecast.weather.gov/MapClick.php?lat=40.6222&lon=-75.3932')
soup = BeautifulSoup(contents.text, 'html.parser')

forecasts = soup.find_all('img', class_='forecast-icon')

for forecast in forecasts:
    print(forecast['alt'])

