import pandas as pd


def merge_all_data(slack_df, notion_df, salesforce_df, repsly_df):

    # --- Slack → activity format ---
    slack_df = slack_df.copy()
    slack_df["record_type"] = "message"
    slack_df["description"] = slack_df["text"]
    slack_df["event_date"] = slack_df["timestamp"]
    slack_df["owner"] = slack_df["user"]

    slack_final = slack_df[[
        "brand", "source", "record_type",
        "description", "owner", "event_date"
    ]]

    # --- Notion → task format ---
    notion_df = notion_df.copy()
    notion_df["record_type"] = "task"
    notion_df["description"] = notion_df["task_name"]
    notion_df["event_date"] = notion_df["due_date"]

    notion_final = notion_df[[
        "brand", "source", "record_type",
        "description", "owner", "event_date"
    ]]

    # --- Salesforce → revenue format ---
    salesforce_df = salesforce_df.copy()
    salesforce_df["record_type"] = "revenue"
    salesforce_df["description"] = salesforce_df["opportunity_stage"]
    salesforce_df["event_date"] = None
    salesforce_df["owner"] = None

    salesforce_final = salesforce_df[[
        "brand", "source", "record_type",
        "description", "owner", "event_date", "revenue"
    ]]

    # --- Repsly → field format ---
    repsly_df = repsly_df.copy()
    repsly_df["record_type"] = "field_visit"
    repsly_df["description"] = repsly_df["store_name"]
    repsly_df["event_date"] = repsly_df["visit_date"]
    repsly_df["owner"] = repsly_df["rep_name"]

    repsly_final = repsly_df[[
        "brand", "source", "record_type",
        "description", "owner", "event_date", "compliance_score"
    ]]

    # --- Combine everything ---
    unified_df = pd.concat([
        slack_final,
        notion_final,
        salesforce_final,
        repsly_final
    ], ignore_index=True)

    return unified_df