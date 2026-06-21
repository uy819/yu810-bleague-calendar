import requests
import pandas as pd
from ics import Calendar, Event

URL = "https://www.bleague.jp/files/user/_/opening2026-27/js/schedule-premier.json"

data = requests.get(URL).json()
df = pd.DataFrame(data)

kings = df[
    (df["home"].str.contains("琉球")) |
    (df["away"].str.contains("琉球"))
]

calendar = Calendar()

for _, row in kings.iterrows():

    e = Event()

    e.name = f"{row['home']} vs {row['away']}"

    e.begin = row["date"]

    e.make_all_day()

    e.location = row["venue"]

    calendar.events.add(e)

with open("kings.ics", "w", encoding="utf-8") as f:
    f.writelines(calendar)

print("ICS生成完了")
