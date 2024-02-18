"""
program
"""
import requests
URL = 'https://api.open-meteo.com/v1/forecast?latitude=51.1801&longitude=71.446&current=temperature_2m&forecast_days=1'
response = requests.get(URL).json()
get = response.get('current')
print(get['temperature_2m'],'C°')
