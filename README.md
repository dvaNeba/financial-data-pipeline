```markdown
# Data Pipeline Project: Stock Prices

## Overview

This project is a production-style data pipeline for financial data (stock prices).  
It fetches data via API, cleans it, stores it in PostgreSQL, calculates analytics, and 
visualizes results.  

**Key Features:**

- Incremental data ingestion  
- PostgreSQL storage  
- Derived metrics calculation (MA20, MA50)  
- Analytics (mean, volatility, min/max)  
- Visualization with proper datetime axis  

---

## Repository Structure

```

data_pipeline_project/
│
├─ README.md
├─ requirements.txt
├─ config.py
├─ main.py
├─ modules/
│   ├─ data_fetcher.py
│   ├─ data_cleaner.py
│   ├─ database.py
│   ├─ analytics.py
│   ├─ analyzer.py
│   └─ visualizer.py
└─ notebooks/
└─ exploration.ipynb

````

- `modules/` — modular, testable code  
- `main.py` — orchestration of pipeline  
- `config.py` — configuration and database settings  
- `notebooks/` — exploration and prototype analysis  

---

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
````

2. Update `config.py` with PostgreSQL credentials and ticker.

3. Run the pipeline:

```bash
python main.py
```

The pipeline will:

* Fetch new stock data from API
* Clean and process data
* Save raw data to PostgreSQL
* Load full dataset
* Calculate moving averages
* Compute analytics (mean, volatility, min, max)
* Plot Close price and MAs

---

## Visualization

* Blue line: Close price
* Orange line: MA 20
* Green line: MA 50

---

## Dependencies

* Python 3.9+
* pandas
* matplotlib
* seaborn
* SQLAlchemy
* yfinance
* psycopg2

---

## Notes

* Derived metrics like MA are not stored in the database, calculated on-the-fly
* Incremental ingestion avoids duplicate data
* `analyzer.py` prints basic statistics for dataset insight

```
```

