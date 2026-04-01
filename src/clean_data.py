import pandas as pd


def clean_slack_data(df):
    df = df.copy()

    # Convert timestamp to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Standardize column names
    df["source"] = "slack"

    return df


def clean_notion_data(df):
    df = df.copy()

    # Convert due_date
    df["due_date"] = pd.to_datetime(df["due_date"])

    # Standardize
    df["source"] = "notion"

    return df


def clean_salesforce_data(df):
    df = df.copy()

    # Ensure revenue is numeric
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")

    df["source"] = "salesforce"

    return df


def clean_repsly_data(df):
    df = df.copy()

    # Convert date
    df["visit_date"] = pd.to_datetime(df["visit_date"])

    # Ensure compliance score numeric
    df["compliance_score"] = pd.to_numeric(df["compliance_score"], errors="coerce")

    df["source"] = "repsly"

    return df