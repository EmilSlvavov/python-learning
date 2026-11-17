import requests

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
TIMEOUT = 10


def find_city(name: str) -> dict | None:
    response = requests.get(GEO_URL, params={"name": name, "count": 1}, timeout=TIMEOUT)
    response.raise_for_status()
    data = response.json()
    results = data.get("results")
    if not results:
        return None
    city = results[0]
    return {"name": city["name"],
            "country": city["country"],
            "latitude": city["latitude"],
            "longitude": city["longitude"]}


def get_weather(latitude: float, longitude: float) -> dict:
    response = requests.get(WEATHER_URL, params={
        "latitude": latitude, "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m"}, timeout=TIMEOUT)
    response.raise_for_status()
    current = response.json()["current"]
    return {"temperature": current["temperature_2m"], "wind_speed": current["wind_speed_10m"]}

def describe(temperature: float) -> str:
    if temperature < 0:
        return "freezing"
    elif temperature < 10:
        return "cold"
    elif temperature < 20:
        return "mild"
    elif temperature < 30:
        return "warm"
    else:
        return "hot"

def main() -> None:
    print("=== Weather ===")
    while True:
        name = input("City (or quit): ").strip()
        if not name:
            print("Please type a city name.")
            continue
        elif name.lower() == "quit":
            print("Bye!")
            break
        else:
            try:
                if city:= find_city(name):
                    w = get_weather(city['latitude'], city['longitude'])
                    print(f"{city['name']}, {city['country']}: {w['temperature']}C, wind {w['wind_speed']} km/h ({describe(w['temperature'])})")
                else:
                    print(f"City not found: {name}")
            except requests.Timeout:
                print("Error: the weather service took too long.")
            except requests.RequestException as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()