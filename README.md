# 🌦️Weather API 
☁️ In this project we have make the use of **weather API** to fetch the present weather condition for city entered.

<h2>🛒Requirement</h2>
<b>Python version</b>
<br>
- Python(3.11.5)<br>
<br>

<b>IDE/Code Editor</b>
<br>
-VS Code

<br>

<h2>📦Tech Stack</h2> <br>
<b> - PYTHON </b>
<br>

**Run the below code in the terminal:**
- This will install all the required libraries.

``` bash
pip install -r requirements.txt
```
<br>


## 📚 Library Used

``` bash 
import requests
import json
import pyttsx3
```

**👩‍💻code**
``` bash
import requests
import json
import pyttsx3

city = input("Enter the name of the city:")
url = f"https://api.weatherapi.com/v1/current.json?key=fe9cc53110ad498093962213252609&q={city}"

weather = requests.get(url)
str_data = (weather.text)


json_text = json.loads(weather.text)  # Deserialize the JSON string into a Python dictionary
w = json_text['current']['temp_c']
print(f"the current weather for {city} is {w} degrees")



engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # female voice
engine.setProperty('rate', 150)            # speed of the voice


engine.say(f"the current weather for {city} is {w} degrees")
engine.runAndWait()

```

<b><p>⭐ If you found this repository useful, consider giving it a star!</p>
<p>Happy Coding 🐍✨</p></b>

👤 Github  : [@droliasakshi12](https://github.com/droliasakshi12)<br>
📩 Email   : sakshidrolia12@gmail.com <br>
🔗 Linkdin : https://www.linkedin.com/in/sakshi-drolia12 <br>

<b><h5>Author</h5></b>
<b>Sakshi Drolia</b>

