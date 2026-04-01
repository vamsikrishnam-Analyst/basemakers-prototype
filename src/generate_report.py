import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "output")


def generate_brand_report(merged_df, salesforce_df, repsly_df, notion_df, brand_name="OLIPOP"):
    brand_merged = merged_df[merged_df["brand"] == brand_name]
    brand_salesforce = salesforce_df[salesforce_df["brand"] == brand_name]
    brand_repsly = repsly_df[repsly_df["brand"] == brand_name]
    brand_notion = notion_df[notion_df["brand"] == brand_name]

    total_revenue = brand_salesforce["revenue"].sum()
    avg_compliance = round(brand_repsly["compliance_score"].mean(), 2)
    open_tasks = brand_notion[brand_notion["status"].isin(["Pending", "In Progress"])].shape[0]
    recent_updates = brand_merged[brand_merged["record_type"] == "message"].head(3)["description"].tolist()

    # Data-driven executive summary
    if avg_compliance >= 90:
        strongest_signal = f"Store execution is strong with an average compliance score of {avg_compliance}."
    elif avg_compliance >= 80:
        strongest_signal = f"Compliance is steady at {avg_compliance} — room to push higher next quarter."
    else:
        strongest_signal = f"Compliance score of {avg_compliance} is below target — needs field attention."

    if open_tasks >= 3:
        biggest_risk = f"{open_tasks} open tasks in Notion risk slowing execution if not resolved this week."
    else:
        biggest_risk = f"{open_tasks} open tasks remaining — operationally in good shape heading into next cycle."

    if total_revenue >= 250000:
        next_action = f"Revenue at ${total_revenue:,.0f} is strong — prioritize expanding store coverage."
    elif total_revenue >= 150000:
        next_action = f"Revenue at ${total_revenue:,.0f} is on track — focus on closing open pipeline opportunities."
    else:
        next_action = f"Revenue at ${total_revenue:,.0f} is below target — review pipeline and accelerate open opportunities."

    report_lines = [
        f"Brand Report: {brand_name}",
        "=" * 60,
        f"Total Revenue            : ${total_revenue:,.0f}",
        f"Average Compliance Score : {avg_compliance}",
        f"Open Tasks               : {open_tasks}",
        "",
        "Executive Summary",
        "-" * 60,
        f"Strongest Signal : {strongest_signal}",
        f"Biggest Risk     : {biggest_risk}",
        f"Next Action      : {next_action}",
        "",
        "Recent Slack Updates",
        "-" * 60,
    ]

    for i, update in enumerate(recent_updates, start=1):
        report_lines.append(f"{i}. {update}")

    report_text = "\n".join(report_lines)

    file_name = f"{brand_name.lower().replace(' ', '_')}_report.txt"
    file_path = os.path.abspath(os.path.join(OUTPUT_PATH, file_name))

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    print("\n--- BRAND REPORT ---")
    print(report_text)
    print(f"\nReport saved to: {file_path}")