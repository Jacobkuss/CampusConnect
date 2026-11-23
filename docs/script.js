
// Search campus events when the user types.
const searchInput = document.getElementById("eventSearch");

if (searchInput) {
    searchInput.addEventListener("input", function () {
        const searchTerm = this.value.toLowerCase();
        const eventCards = document.querySelectorAll(".event-card");
        let visibleEvents = 0;

        eventCards.forEach(function (card) {
            const eventText = card.textContent.toLowerCase();

            if (eventText.includes(searchTerm)) {
                card.style.display = "";
                visibleEvents++;
            } else {
                card.style.display = "none";
            }
        });

        document.getElementById("noEvents").hidden = visibleEvents > 0;
    });
}

// Convert weather codes into readable descriptions.
function getWeatherDescription(code) {
    if (code === 0) return "Clear sky";
    if ([1, 2, 3].includes(code)) return "Partly cloudy";
    if ([45, 48].includes(code)) return "Foggy";
    if ([51, 53, 55, 61, 63, 65].includes(code)) return "Rain";
    if ([71, 73, 75].includes(code)) return "Snow";
    if ([80, 81, 82].includes(code)) return "Rain showers";
    if ([95, 96, 99].includes(code)) return "Thunderstorms";
    return "Conditions unavailable";
}

// Fetch live weather from the Open-Meteo API.
async function getWeather() {
    const status = document.getElementById("weatherStatus");

    if (!status) return;

    status.textContent = "Loading weather data...";

    const url = "https://api.open-meteo.com/v1/forecast?latitude=34.2746&longitude=-81.6187&current=temperature_2m,wind_speed_10m,weather_code&temperature_unit=fahrenheit&wind_speed_unit=mph&timezone=America%2FNew_York";

    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error("Weather request failed");
        }

        const data = await response.json();
        const current = data.current;

        document.getElementById("temperature").textContent =
            current.temperature_2m + " °F";

        document.getElementById("conditions").textContent =
            getWeatherDescription(current.weather_code);

        document.getElementById("wind").textContent =
            "Wind: " + current.wind_speed_10m + " mph";

        status.textContent = "Weather updated successfully!";
    } catch (error) {
        status.textContent = "Unable to load weather. Please try again.";
        console.error("Weather error:", error);
    }
}

// Load weather automatically when the weather page opens.
if (document.getElementById("weatherStatus")) {
    getWeather();
}
