
from selenium import webdriver
from bs4 import BeautifulSoup
import sqlite3
import time
import re


class CampusEventScraper:

    def __init__(self, events_url):
        self.events_url = events_url
        self.database_path = "db/campusconnect.db"

    def fetch_calendar(self):
        driver = webdriver.Chrome()

        try:
            driver.get(self.events_url)
            time.sleep(8)
            html = driver.page_source
            print("Website loaded successfully!")
            return html

        finally:
            driver.quit()

    def scrape_events(self):
        html = self.fetch_calendar()
        soup = BeautifulSoup(html, "html.parser")

        # Find the individual event cards
        event_cards = soup.find_all("li", class_="py-2")

        events = []

        for card in event_cards:
            # Get the individual pieces of text from the card
            texts = [text.strip() for text in card.stripped_strings]

            # Find the event date
            date_index = next(
                (
                    i for i, text in enumerate(texts)
                    if re.search(
                        r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun),\s+[A-Z][a-z]{2}\s+\d{1,2}",
                        text
                    )
                ),
                None
            )

            if date_index is None:
                continue

            event_date = texts[date_index]

            # The next text items contain the category and title
            details = texts[date_index + 1:]

            if len(details) < 2:
                continue

            category = details[0]
            title = details[1]

            # Find the college name and the location after it
            location = "Unknown"

            if "Adrian College" in details:
                college_index = details.index("Adrian College")

                if college_index + 1 < len(details):
                    location = details[college_index + 1]

            events.append((
                title,
                event_date,
                location,
                category
            ))

        # Save the scraped events to SQLite
        if events:
            conn = sqlite3.connect(self.database_path)
            cursor = conn.cursor()

            cursor.execute("DELETE FROM external_events")

            cursor.executemany(
                """
                INSERT INTO external_events
                (title, date, location, description)
                VALUES (?, ?, ?, ?)
                """,
                events
            )

            conn.commit()
            conn.close()

        print("Events found:", len(events))
        print("Events saved to the database!")

        return events


if __name__ == "__main__":

    scraper = CampusEventScraper(
        "https://events.hometownticketing.com/boxoffice/adriancollege"
    )

    scraper.scrape_events()
