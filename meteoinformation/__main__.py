import os

import requests

city = "Moscow,RU"
appid = os.getenv("APP_ID")

if __name__ == "__main__":
	res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={
		"q": city, "units": "metric", "lang": "ru", "APPID": appid
	})
	data = res.json()

	print("Город:", city)
	print("Погодные условия:", data["weather"][0]["description"])
	print("Температура:", data["main"]["temp"])
	print("Минимальная температура:", data["main"]["temp_min"])
	print("Максимальная температура:", data["main"]["temp_max"])
	print("Видимость (м):", data["visibility"])
	print("Скорость ветра (м/c):", data["wind"]["speed"])

	res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={
		"q": city, "units": "metric", "lang": "ru", "APPID": appid
	})
	data = res.json()

	print("Прогноз погоды на неделю")
	for element in data["list"]:
		print(f"Дата <{element['dt_txt']}>")
		print("Температура <{0:+3.0f}>".format(element["main"]["temp"]))
		print(f"Видимость (м) <{element['visibility']}>")
		print(f"Скорость ветра (м/с) <{element['wind']['speed']}>")
		print(f"Погодные условия <{element['weather'][0]['description']}>")
		print("_____________________________")