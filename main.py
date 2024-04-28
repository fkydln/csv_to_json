# Homework: Write a CSV-to-JSON translator that expects the path to a CSV file as argument, and for each line in the
# file, prints out a JSON object encapsulating that record
import csv
import json
import sys


def csv_to_json(csv_file):
    with open(csv_file, 'r') as file:  # Open the CSV file

        csv_reader = csv.DictReader(file)  # Create a CSV reader

        for row in csv_reader:  # Iterate over each row in the CSV file

            json_data = json.dumps(row)  # Convert each row to JSON
            print(json_data)


if len(sys.argv) != 2:  # Check if the CSV file path is provided as argument
    print("Usage: python csv_to_json.py <csv_file>")
    sys.exit(1)

csv_file = sys.argv[1]
csv_to_json(csv_file)
