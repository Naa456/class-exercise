import json
import logging
from pathlib import Path
from random import sample
import pandas as pd
import yaml
import os
from dotenv import load_dotenv
logging.basicConfig(
 level=logging.INFO,
 format="%(asctime)s %(levelname)-8s %(message)s",
 datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)
#def inspect_csv(filepath):
#    """Read a CSV file and display basic information."""
#    # TODO:
#    # 1. Read the file using pd.read_csv().
#    # 2. Log the filepath at INFO.
#    # 3. Print the first three rows (e.g. DataFrame.head(3))
#    pass
def inspect_csv(filepath):
    """Read a CSV file and display basic information."""
    df = pd.read_csv(filepath)
    logger.info(f"Inspecting CSV: {filepath.name}")
    print(df.head(3))
pass

#def inspect_json(filepath):
 """Read a JSON file and display basic information."""
 # TODO:
 # 1. Open the file and read it using json.load().
 # 2. Log the filepath at INFO.
 # 3. Print the contents.
 #pass

def inspect_json(filepath):
  """Read a JSON file and display basic information."""
  with open(filepath, "r") as f:
      data = json.load(f)
  logger.info(f"Inspecting JSON: {filepath}")
  print(data)
pass
  
#def inspect_yaml(filepath):
"""Read a YAML file and display basic information."""
 # TODO:
 # 1. Open the file and read it using yaml.safe_load().
 # 2. Log the filepath at INFO.
 # 3. Print the contents.
def inspect_yaml(filepath):
  """Read a YAML file and display basic information."""
  with open(filepath, "r") as f:
      data = yaml.safe_load(f)
  logger.info(f"Inspecting YAML: {filepath}")
  #lets automate it by logging.info(everything but do filepath.suffix)
  print(data)
pass


def inspect_env():
 """Read a .env file and display basic information."""
 load_dotenv()
 keys = [
 key for key in ["USERNAME", "PASSWORD"]
 if os.getenv(key) is not None
 ]
 # TODO:
 # 1. Log at INFO that .env was loaded.
 # 2. Print keys.
 # Do not print passwords, API keys, or other secret va

load_dotenv()
keys=[key for key in ["USERNAME", "PASSWORD"] if os.getenv(key) is not None]

 logger.info(".env file loaded")
 print(keys)
pass



filepath_csv=data_dir/sample.csv
filepath_json=data_dir/sample.json
filepath_yaml=data_dir/sample.yaml
#we are doing concactinat ion

inspect_csv(filepath_csv)
inspect_json(filepath_json)
inspect_yaml(filepath_yaml)
inspect_env()#this is to call the function