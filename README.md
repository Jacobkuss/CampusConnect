# CampusConnect

CampusConnect is a student-focused application that displays campus events and weather information.

## Features

- **Campus Event Scraper:** Uses Selenium and BeautifulSoup to collect event information from the Adrian College events website.
- **Weather API Integration:** Uses the Open-Meteo API to retrieve a seven-day weather forecast for Newberry, South Carolina.
- **SQLite Database:** Stores internal events, externally scraped events, and weather information.
- **Flask Application:** Displays event and weather information through web pages.

## Setting Up the Project

### 1. Install Dependencies

Install the required Python packages:

```bash
py -m pip install flask requests beautifulsoup4 selenium
```

### 2. Initialize the Database

Run the database seeding script:

```bash
py db/seed_data.py
```

This creates the database tables and inserts starter data.

### 3. Run the Event Scraper

To retrieve and store campus events:

```bash
py utils/event_scraper.py
```

### 4. Retrieve Weather Data

To retrieve and store the weather forecast:

```bash
py utils/api_client.py
```

### 5. Start the Application

Run the Flask application:

```bash
py app.py
```

Open the application in your browser at:

`http://127.0.0.1:5000/`

## Application Pages

- `/` — Main dashboard
- `/events` — Internal and externally scraped campus events
- `/api` — Seven-day weather forecast

## Technologies Used

- Python
- Flask
- SQLite
- Selenium
- BeautifulSoup
- Requests
- Open-Meteo API

## AI Assistance

ChatGPT was used as a development assistant to help with code implementation, debugging, database integration, web scraping, API integration, and documentation. The generated code was reviewed, adapted, and tested as part of the project development process.