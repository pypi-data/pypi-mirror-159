import json

import sqlite3
from pathlib import Path
dictn = [{"id": 1, 'Title': 'Kayamat', 'Year': 1995}, {
    "id": 1, 'Title': 'Kayamat', 'Year': 1995}, {"id": 1, 'Title': 'Kayamat', 'Year': 1995}]

# json_obj = json.dumps(dictn)                          #to write json data to file
# with Path('movies.json') as file:
#     file.write_text(json_obj)

with Path('movies.json') as file:  # to read json data to file
    json_obj = file.read_text()
    movies = json.loads(json_obj)
with sqlite3.connect("db.sqlite3") as db:
    command = "INSERT INTO Movies VALUES(?,?,?)"
    for movie in movies:
        db.execute(command, movie.values())
    db.commit()
