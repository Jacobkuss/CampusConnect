
-- SQLite schema

-- Drop existing tables so the database can be recreated
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS external_events;
DROP TABLE IF EXISTS api_data;

-- Users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    preferences TEXT
);

-- Original internal events table
CREATE TABLE events (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    location TEXT,
    date TEXT
);

-- Stores events scraped from the college website
CREATE TABLE external_events (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    date TEXT,
    location TEXT,
    description TEXT
);

-- Stores weather information from Open-Meteo
CREATE TABLE api_data (
    id INTEGER PRIMARY KEY,
    forecast_date TEXT,
    temperature REAL,
    wind_speed REAL,
    weather_condition TEXT
);
