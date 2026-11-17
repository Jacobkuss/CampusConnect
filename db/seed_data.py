
import sqlite3

DB_PATH = "db/campusconnect.db"

# Connect to the CampusConnect database
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Create all database tables using schema.sql
with open("db/schema.sql", "r") as schema_file:
    conn.executescript(schema_file.read())

# Create Users Seed Data
c.execute("INSERT INTO users (name, preferences) VALUES (?, ?)",
          ("Alice", "Aly"))
c.execute("INSERT INTO users (name, preferences) VALUES (?, ?)",
          ("Bob", "art, Bobby"))
c.execute("INSERT INTO users (name, preferences) VALUES (?, ?)",
          ("Charlie", "Chaz"))

# Internal Events Seed Data
c.execute("INSERT INTO events (title, location, date) VALUES (?, ?, ?)",
          ("Music Night", "Student Center", "2025-04-05"))
c.execute("INSERT INTO events (title, location, date) VALUES (?, ?, ?)",
          ("Hackathon", "Library", "2025-04-01"))
c.execute("INSERT INTO events (title, location, date) VALUES (?, ?, ?)",
          ("Art Exhibition", "Gallery", "2025-04-10"))

# Sample external college events
c.execute("""
    INSERT INTO external_events
    (title, date, location, description)
    VALUES (?, ?, ?, ?)
""", ("Campus Welcome Event", "2026-11-20", "Newberry College",
      "A welcome event for students."))

c.execute("""
    INSERT INTO external_events
    (title, date, location, description)
    VALUES (?, ?, ?, ?)
""", ("Student Activities Day", "2026-11-22", "Campus Center",
      "A day of activities for students."))

# Sample weather data from Open-Meteo
c.execute("""
    INSERT INTO api_data
    (forecast_date, temperature, wind_speed, weather_condition)
    VALUES (?, ?, ?, ?)
""", ("2026-11-20", 68.0, 8.5, "Partly cloudy"))

c.execute("""
    INSERT INTO api_data
    (forecast_date, temperature, wind_speed, weather_condition)
    VALUES (?, ?, ?, ?)
""", ("2026-11-21", 72.0, 5.2, "Sunny"))

# Save all changes and close the database
conn.commit()
conn.close()

print("CampusConnect database initialized successfully!")
