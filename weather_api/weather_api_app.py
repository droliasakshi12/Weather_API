import requests
import json
import pyttsx3

city = input("Enter the name of the city:")
url = f"https://api.weatherapi.com/v1/current.json?key=fe9cc53110ad498093962213252609&q={city}"

weather = requests.get(url)
str_data = (weather.text)

# converting the string data above into json format

json_text = json.loads(weather.text)  # loads the string
w = json_text['current']['temp_c']
print(f"the current weather for {city} is {w} degrees")


engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # female voice
engine.setProperty('rate', 150)            # speed of the voice


engine.say(f"the current weather for {city} is {w} degrees")

engine.runAndWait()
