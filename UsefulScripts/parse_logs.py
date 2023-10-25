import re

log_text = """24/Oct/2023:19:41:42 -0500 INFO User ArtisticSoul22 successfully logged in.
24/Oct/2023:19:41:42 -0500 WARNING Failed login attempt for user DEBUG from IP CoffeeAddict28.
24/Oct/2023:19:41:42 -0500 INFO User session started: TechNinja007"""

log_entries = []
pattern = r'(\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2} [-+]\d{4})\s(\w+)\s(.+)'

for line in log_text.split('\n'):
    match = re.match(pattern, line)
    if match:
        timestamp, log_level, message = match.groups()
        log_entries.append([timestamp, log_level, message])

for entry in log_entries:
    print(entry)
