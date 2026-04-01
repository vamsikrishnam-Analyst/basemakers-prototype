import pandas as pd
import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data")


def load_slack_data():
    file_path = os.path.join(DATA_PATH, "slack_data.json")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)


def load_notion_data():
    file_path = os.path.join(DATA_PATH, "notion_data.json")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)


def load_salesforce_data():
    file_path = os.path.join(DATA_PATH, "salesforce_data.csv")
    return pd.read_csv(file_path)


def load_repsly_data():
    file_path = os.path.join(DATA_PATH, "repsly_data.csv")
    return pd.read_csv(file_path)