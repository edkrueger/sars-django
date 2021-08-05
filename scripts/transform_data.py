"""Prepares the data from a Django's loaddata."""
import os
import csv
import json

CSV_PATH = "data/sars_2003_complete_dataset_clean.csv"
MODEL = "sars.record"
JSON_PATH = "app/sars/fixtures/data.json"

dirs, _ = os.path.split(JSON_PATH)
os.makedirs(dirs, exist_ok=True)

transformed_data = []

with open(CSV_PATH, "r") as csv_file:

    dict_reader = csv.DictReader(csv_file)

    for i, row in enumerate(dict_reader):
        transformed_row = {
            "model": MODEL,
            "pk": i,
            "fields": {
                "date": row["date"],
                "country": row["country"],
                "cases": row["cases"],
                "deaths": row["deaths"],
                "recoveries": row["recoveries"],
            },
        }
        transformed_data.append(transformed_row)

with open(JSON_PATH, "w+") as json_file:
    json_file.write(json.dumps(transformed_data))
