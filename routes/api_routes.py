
from flask import Blueprint, render_template
import sqlite3

api_bp = Blueprint('api', __name__)

@api_bp.route("/api")
def api():
    conn = sqlite3.connect("db/campusconnect.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT forecast_date, temperature, wind_speed, weather_condition
        FROM api_data
        ORDER BY forecast_date
    """)

    weather_data = cursor.fetchall()

    conn.close()

    return render_template("api.html", weather_data=weather_data)

