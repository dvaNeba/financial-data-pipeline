# 📊 Financial Data Pipeline Project

Production-style data pipeline for financial market data analysis.

## 🚀 Project Overview

This project automatically:
- Fetches stock data via API
- Cleans and processes data
- Performs statistical analysis
- Generates visualizations
- Saves processed datasets

Example asset: AAPL (Apple Inc.)

---

## 🛠 Tech Stack

- Python
- Pandas
- yfinance
- Matplotlib / Seaborn
- Logging
- Modular architecture

---

## 📂 Project Structure

data_pipeline_project/
│
├─ main.py
├─ config.py
├─ requirements.txt
├─ modules/
│   ├─ data_fetcher.py
│   ├─ data_cleaner.py
│   ├─ analyzer.py
│   └─ visualizer.py
└─ data/
    ├─ raw/
    └─ processed/

---

## ▶️ How to Run

1. Install dependencies:

pip install -r requirements.txt


2. Run pipeline:

python main.py


---

## 📈 Output

- Cleaned dataset in `/data/processed`
- Price chart with moving averages
- Basic statistical metrics

---

## 🔮 Future Improvements

- Database storage (PostgreSQL)
- Docker containerization
- CI/CD integration
- Automated scheduling (cron/Airflow)

