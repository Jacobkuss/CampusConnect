
import requests
import sqlite3


class APIClient:

    def __init__(self):
        self.url = "https://api.open-meteo.com/v1/forecast"
        self.database_path = "db/campusconnect.db"

        # Coordinates for Newberry, South Carolina
        self.parameters = {
            "latitude": 34.2746,
            "longitude": -81.6187,
            "daily": [
                "weather_code",
                "temperature_2m_max",
                "wind_speed_10m_max"
            ],
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "timezone": "America/New_York",
            "forecast_days": 7
        }

    def get_weather(self):
        response = requests.get(
            self.url,
            params=self.parameters,
            timeout=15
        )

        response.raise_for_status()
        return response.json()

    def save_weather(self, weather_data):
        daily = weather_data["daily"]

        weather_descriptions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Heavy drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            71: "Slight snow",
            73: "Moderate snow",
            75: "Heavy snow",
            80: "Rain showers",
            81: "Moderate rain showers",
            82: "Heavy rain showers",
            95: "Thunderstorm"
        }

        records = []

        for i in range(len(daily["time"])):
            date = daily["time"][i]
            temperature = daily["temperature_2m_max"][i]
            wind_speed = daily["wind_speed_10m_max"][i]
            weather_code = daily["weather_code"][i]

            condition = weather_descriptions.get(
                weather_code,
                "Unknown"
            )

            records.append((
                date,
                temperature,
                wind_speed,
                condition
            ))

        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM api_data")

        cursor.executemany(
            """
            INSERT INTO api_data
            (forecast_date, temperature, wind_speed, weather_condition)
            VALUES (?, ?, ?, ?)
            """,
            records
        )

        conn.commit()
        conn.close()

        print("Weather records saved:", len(records))


if __name__ == "__main__":
    client = APIClient()

    weather = client.get_weather()
    client.save_weather(weather)

    print("Weather API successfully connected!")
