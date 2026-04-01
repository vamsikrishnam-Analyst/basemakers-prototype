# Basemakers Prototype Pipeline

A working data pipeline that pulls from four sources, cleans and merges the data, and generates a brand-level report.

---

## Why I Built This

One thing that came up in our conversation was how data ends up scattered across tools like Slack, Notion, Salesforce, and Repsly. Each team has their own view, and pulling it all together takes a lot of manual work.

I wanted to show how I would actually approach that problem. So I built a small pipeline that ingests data from those four sources, standardizes it, stores it in SQLite, and generates a clean report for any brand partner.

Pipeline flow:
Slack JSON + Notion JSON + Salesforce CSV + Repsly CSV → Python pipeline → SQLite → Brand Report

---

## What It Does

- Loads data from four sources: Slack, Notion, Salesforce, Repsly
- Cleans and standardizes each source into a consistent format
- Runs basic validation checks to catch missing or bad data
- Merges everything into one unified reporting layer
- Stores all tables in SQLite so you can run SQL queries against them
- Generates a brand report for any brand partner with one command

---

## Data Sources

- Slack — team messages, brand updates, field alerts
- Notion — open tasks, owners, due dates, status
- Salesforce — revenue, opportunity stage, region
- Repsly — store visits, compliance scores, field rep names

---

## How the Pipeline Runs

1. Load data from all four sources into pandas DataFrames
2. Clean each source, normalize brand names, handle missing values
3. Run validation checks and flag any issues
4. Merge all sources into one unified activity table
5. Write everything to SQLite
6. Run SQL queries for revenue, compliance, and task summaries
7. Generate a brand report for the selected brand

---

## Sample Output

Brand Report for OLIPOP:
```
Brand                    : OLIPOP

Revenue
Total Revenue            : $293,000
Opportunity Stages       : 2x Closed Won, 1x Negotiation

Field Execution
Total Store Visits       : 5
Average Compliance Score : 88.8
Lowest Store             : Sprouts Scottsdale (78)
Highest Store            : Whole Foods Pasadena (95)

Open Tasks
- Finalize Q4 promo calendar           [In Progress - Sarah K]
- Submit shelf reset photos 12 stores  [Pending - Field Team]
- Review new SKU placement strategy    [Pending - Nick D]

Slack Updates
- OLIPOP confirmed expansion to 50 new Target doors in Southwest
- Vintage Cola SKU running 23% ahead of velocity targets
- 3 Sprouts locations flagged non-compliant after promo reset

Summary
Strongest signal : Vintage Cola SKU outperforming in Southwest
Biggest risk     : 3 Sprouts locations flagged after promo reset
Next action      : Deploy field team to stores with pending shelf resets
```

---

## SQL Examples

Total revenue by brand:
```sql
SELECT brand, SUM(revenue) AS total_revenue
FROM salesforce_data
GROUP BY brand
ORDER BY total_revenue DESC;
```
```
OLIPOP           293000
Honey Stinger    243000
C20              242000
Guayaki          215000
Nixie            165000
```

Average compliance score by brand:
```sql
SELECT brand, ROUND(AVG(compliance_score), 1) AS avg_compliance
FROM repsly_data
GROUP BY brand
ORDER BY avg_compliance DESC;
```
```
Honey Stinger    92.8
OLIPOP           88.8
Nixie            86.6
Guayaki          79.2
C20              76.8
```

---

## Project Structure
```
basemakers_prototype/
├── data/
│   ├── slack_data.json
│   ├── notion_data.json
│   ├── salesforce_data.csv
│   └── repsly_data.csv
├── output/
│   ├── basemakers_demo.db
│   ├── olipop_report.txt
│   └── validation_report.txt
├── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── validate_data.py
│   ├── merge_data.py
│   ├── sql_layer.py
│   ├── generate_report.py
│   └── main.py
├── README.md
└── requirements.txt
```

---

## How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run for OLIPOP (default)
python src/main.py

# Run for any brand
python src/main.py Guayaki
python src/main.py Nixie
python src/main.py C20
python src/main.py "Honey Stinger"
```

---

## How This Connects to Basemakers

Data spread across Slack, Notion, Salesforce, Repsly → this pipeline pulls it all into one place

Brand managers pulling reports manually → one command generates the full report

No single source of truth → everything merges into one SQLite layer

Compliance hard to track across stores → surfaces scores by brand and store via SQL

Open tasks buried in Notion → included in every brand report automatically

---

## Tech Stack

- Python
- pandas
- sqlite3
- GitHub