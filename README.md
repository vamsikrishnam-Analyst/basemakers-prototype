# Basemakers Prototype Pipeline
End-to-end data pipeline simulating multi-source business data integration and reporting.

## Key Highlights

- Built an end-to-end data pipeline integrating four business systems (Slack, Notion, Salesforce, Repsly)
- Processed and standardized both structured and unstructured data for analysis
- Designed a unified reporting layer to support cross-functional decision-making
- Implemented SQL-based analytics for revenue, compliance, and operational tracking
- Generated automated, stakeholder-ready brand reports with clear business insights

## Overview

This project simulates how fragmented operational data from tools like Slack, Notion, Salesforce, and field execution platforms can be consolidated into a single reporting layer.

The use case reflects a real-world environment where business teams rely on multiple systems for communication, operations, revenue tracking, and field execution.

## Data Sources

- Slack updates (unstructured communication)
- Notion tasks (operational tracking)
- Salesforce opportunities (revenue data)
- Repsly field visit data (store execution)

## Pipeline Workflow

1. Loads JSON and CSV data from multiple sources  
2. Cleans and standardizes the data  
3. Runs validation checks for quality and consistency  
4. Merges all sources into a unified reporting layer  
5. Stores processed data in SQLite  
6. Executes SQL queries for business insights  
7. Generates a stakeholder-ready brand report  

## Project Structure

```
basemakers_prototype/
├── data/
├── output/
├── src/
├── README.md
├── requirements.txt
```

## How to Run

```bash
python src/main.py
