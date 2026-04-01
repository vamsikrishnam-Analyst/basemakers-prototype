from load_data import (
    load_slack_data,
    load_notion_data,
    load_salesforce_data,
    load_repsly_data
)
from clean_data import (
    clean_slack_data,
    clean_notion_data,
    clean_salesforce_data,
    clean_repsly_data
)
from validate_data import (
    validate_slack_data,
    validate_notion_data,
    validate_salesforce_data,
    validate_repsly_data
)
from merge_data import merge_all_data
from sql_layer import save_to_sqlite, run_sql_queries
from generate_report import generate_brand_report


def main():
    print("\n=== BASEMAKERS PROTOTYPE PIPELINE STARTED ===")

    slack_df = load_slack_data()
    notion_df = load_notion_data()
    salesforce_df = load_salesforce_data()
    repsly_df = load_repsly_data()

    print("\nData loaded successfully")

    slack_clean = clean_slack_data(slack_df)
    notion_clean = clean_notion_data(notion_df)
    salesforce_clean = clean_salesforce_data(salesforce_df)
    repsly_clean = clean_repsly_data(repsly_df)

    print("Data cleaned successfully")

    validate_slack_data(slack_clean)
    validate_notion_data(notion_clean)
    validate_salesforce_data(salesforce_clean)
    validate_repsly_data(repsly_clean)

    print("\nValidation completed successfully")

    merged_df = merge_all_data(
        slack_clean,
        notion_clean,
        salesforce_clean,
        repsly_clean
    )

    print("Merged reporting layer created successfully")

    save_to_sqlite(
        slack_clean,
        notion_clean,
        salesforce_clean,
        repsly_clean,
        merged_df
    )

    print("Saved all tables to SQLite database")

    run_sql_queries()

    generate_brand_report(
        merged_df,
        salesforce_clean,
        repsly_clean,
        notion_clean,
        brand_name="OLIPOP"
    )

    print("\n=== PIPELINE COMPLETED SUCCESSFULLY ===")


if __name__ == "__main__":
    main()