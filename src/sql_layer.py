import sqlite3
import pandas as pd
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "output")
DB_PATH = os.path.join(OUTPUT_PATH, "basemakers_demo.db")


def save_to_sqlite(slack_df, notion_df, salesforce_df, repsly_df, merged_df):
    conn = sqlite3.connect(DB_PATH)

    # Make copies so original dataframes stay unchanged
    slack_df = slack_df.copy()
    notion_df = notion_df.copy()
    salesforce_df = salesforce_df.copy()
    repsly_df = repsly_df.copy()
    merged_df = merged_df.copy()

    # Convert datetime columns to strings for SQLite
    if "timestamp" in slack_df.columns:
        slack_df["timestamp"] = slack_df["timestamp"].astype(str)

    if "due_date" in notion_df.columns:
        notion_df["due_date"] = notion_df["due_date"].astype(str)

    if "visit_date" in repsly_df.columns:
        repsly_df["visit_date"] = repsly_df["visit_date"].astype(str)

    if "event_date" in merged_df.columns:
        merged_df["event_date"] = merged_df["event_date"].astype(str)

    slack_df.to_sql("slack_data", conn, if_exists="replace", index=False)
    notion_df.to_sql("notion_data", conn, if_exists="replace", index=False)
    salesforce_df.to_sql("salesforce_data", conn, if_exists="replace", index=False)
    repsly_df.to_sql("repsly_data", conn, if_exists="replace", index=False)
    merged_df.to_sql("merged_data", conn, if_exists="replace", index=False)

    conn.close()


def run_sql_queries():
    conn = sqlite3.connect(DB_PATH)

    print("\n--- SQL QUERY: Total Revenue by Brand ---")
    query_1 = """
    SELECT brand, SUM(revenue) AS total_revenue
    FROM salesforce_data
    GROUP BY brand
    ORDER BY total_revenue DESC
    """
    print(pd.read_sql_query(query_1, conn))

    print("\n--- SQL QUERY: Average Compliance Score by Brand ---")
    query_2 = """
    SELECT brand, ROUND(AVG(compliance_score), 2) AS avg_compliance_score
    FROM repsly_data
    GROUP BY brand
    ORDER BY avg_compliance_score DESC
    """
    print(pd.read_sql_query(query_2, conn))

    print("\n--- SQL QUERY: Open Notion Tasks by Brand ---")
    query_3 = """
    SELECT brand, COUNT(*) AS open_tasks
    FROM notion_data
    WHERE status IN ('Pending', 'In Progress')
    GROUP BY brand
    ORDER BY open_tasks DESC
    """
    print(pd.read_sql_query(query_3, conn))

    conn.close()