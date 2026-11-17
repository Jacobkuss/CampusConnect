
import os
import sqlite3
from flask import Blueprint, render_template

event_bp = Blueprint('event', __name__)

DB_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'db', 'campusconnect.db')
)

@event_bp.route("/events")
def events():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Fetch internal events
    cursor.execute("SELECT title, location, date FROM events")
    internal_events = cursor.fetchall()

    # Fetch externally scraped events
    cursor.execute("""
        SELECT title, location, date, description
        FROM external_events
        ORDER BY date
    """)
    external_events = cursor.fetchall()

    conn.close()

    return render_template(
        "events.html",
        internal_events=internal_events,
        external_events=external_events
    )
