# Basemakers Prototype Pipeline

This project is a small end-to-end prototype that simulates how scattered operational data can be brought into one unified reporting layer.

It uses four simulated data sources:
- Slack updates
- Notion tasks
- Salesforce opportunities
- Repsly field visit data

The pipeline does the following:
1. Loads JSON and CSV data from multiple sources
2. Cleans and standardizes the data
3. Runs validation checks for quality and consistency
4. Merges all sources into a unified reporting layer
5. Saves the data into SQLite
6. Runs SQL queries for reporting
7. Generates a stakeholder-ready brand report

## Project Structure

```text
basemakers_prototype/
├── data/
├── output/
├── src/
├── README.md
├── requirements.txt