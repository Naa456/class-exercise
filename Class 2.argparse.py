import argparse
from html import parser

parser = argparse.ArgumentParser()
parser.add_argument(
    "--input","-i",#we we wite a name fucntgion,the user can either use the double dash or single dash.
    required=True,
    help="path to input CSV file")

parser.add_argument(
    "--output","-o",
    required=True,
    help="path to output CSV file"
)



parser.add_argument("--verbose","-v", 
    action="store_true",
    help="print detailed information about the process")
#this is to ansalyse a data file

args=parser.parse_args()

pd.read_csv(input_data)


```python
import argparse
import csv
import sys
from pathlib import Path

def check_data(filename):
    """Read the CSV file and check for missing values."""
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    header = rows[0]
    data = rows[1:]
    missing_rows = []

    for row_number, row in enumerate(data, start=2):
        if any(value == "" for value in row):
            missing_rows.append(row_number)

    return header, data, missing_rows


# TODO 1: Create an ArgumentParser
# Description: "Check the quality of a CSV file."
parser=argparse.ArgumentParser(description="Check the quality of the CSV FILE")

# TODO 2: Add a named argument (required):
# Long form: --input
# Short form: -i
# Help: "CSV file to check
parser.add_argument(
    "-- input", "--i"
    required=True,
    help="CSV file to check"
)


# TODO 3: Add an named argument (optional):
# Long form: --output
# Short form: -o
# Default: "data_quality.txt"
# Help: "Output report filename"

parser.add_argument(
    "--output", "-o",
    default="data_quality.txt",
    help="Output report filename"
)


# TODO 4: Add a boolean flag:
# Long form: --verbose
# Short form: -v
# Use action="store_true"
# Help: "Show detailed DEBUG messages"

