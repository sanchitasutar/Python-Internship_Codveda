import requests

city = input("Enter city: ")
api_key = "YOUR_API_KEY"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error:", response.status_code)
    print(response.text)
