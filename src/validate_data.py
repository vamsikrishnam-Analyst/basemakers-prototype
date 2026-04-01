import pandas as pd


def validate_slack_data(df):
    print("\nValidating Slack Data...")

    if df["brand"].isnull().sum() > 0:
        print("⚠️ Missing brand values in Slack data")

    if df.duplicated().sum() > 0:
        print("⚠️ Duplicate rows found in Slack data")

    print("Slack validation complete")


def validate_notion_data(df):
    print("\nValidating Notion Data...")

    if df["task_name"].isnull().sum() > 0:
        print("⚠️ Missing task names")

    if df["status"].isnull().sum() > 0:
        print("⚠️ Missing task status")

    print("Notion validation complete")


def validate_salesforce_data(df):
    print("\nValidating Salesforce Data...")

    if (df["revenue"] < 0).any():
        print("⚠️ Negative revenue values found")

    if df["revenue"].isnull().sum() > 0:
        print("⚠️ Missing revenue values")

    print("Salesforce validation complete")


def validate_repsly_data(df):
    print("\nValidating Repsly Data...")

    if (df["compliance_score"] < 0).any() or (df["compliance_score"] > 100).any():
        print("⚠️ Invalid compliance scores")

    if df["compliance_score"].isnull().sum() > 0:
        print("⚠️ Missing compliance scores")

    print("Repsly validation complete")