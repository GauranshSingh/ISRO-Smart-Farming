import requests


def get_weather(latitude, longitude):

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,rain"
    )

    response = requests.get(url)

    data = response.json()

    current = data["current"]

    return {
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "rain": current["rain"]
    }