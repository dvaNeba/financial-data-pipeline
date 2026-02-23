```markdown
# Financial Data Pipeline (Python + PostgreSQL)

This project demonstrates a production-style financial data pipeline built with Python and PostgreSQL.

It incrementally fetches market data via API, cleans and stores it in a relational database, computes analytical metrics, and visualizes results. The system is modular, configurable via CLI, and designed to reflect real-world data engineering and automation practices.

---

## 🚀 Key Capabilities

- Incremental data ingestion (only new records are fetched)
- API integration (yfinance)
- Data cleaning and validation
- Persistent storage in PostgreSQL
- Analytical metrics:
  - Moving averages (MA20, MA50)
  - Volatility
  - Min/Max price
- Visualization with Matplotlib/Seaborn
- CLI-driven execution (ticker and date overrides)
- Modular architecture
- Logging for operational monitoring
- Interactive exploration via Jupyter Notebook

---

## 🏗 Architecture Overview

The pipeline follows this flow:

API → Raw Data → Cleaning → PostgreSQL Storage → Analytics → Visualization

Key characteristics:

- Incremental updates based on latest DB date
- Separation of concerns (fetching, cleaning, DB, analytics, visualization)
- Configuration management via `config.py`
- CLI overrides for flexible execution
- Structured logging

---

## 📂 Repository Structure

```

data_pipeline_project/
├─ assets/
│   └─ plot_example.png
├─ config.py
├─ main.py
├─ modules/
│   ├─ data_fetcher.py
│   ├─ data_cleaner.py
│   ├─ database.py
│   ├─ analytics.py
│   ├─ analyzer.py
│   └─ visualizer.py
├─ notebooks/
│   └─ exploration.ipynb
├─ requirements.txt
└─ README.md

````

---

## ⚙ Installation

```bash
git clone https://github.com/<your-username>/<repo>.git
cd data_pipeline_project
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

---

## 🔧 Configuration

Edit `config.py`:

```python
TICKER = "AAPL"
START_DATE = "2022-01-01"

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "stocks",
    "user": "your_user",
    "password": "your_password"
}
```

CLI arguments override config values.

---

## ▶ Usage

### Default execution (uses config values)

```bash
python main.py
```

### Specify ticker

```bash
python main.py --ticker MSFT
```

### Specify full date range

```bash
python main.py --ticker NVDA --start 2023-01-01 --end 2023-12-31
```

If no start date is provided, the pipeline automatically detects the latest stored date in PostgreSQL and fetches only missing data.

---

## 🗄 Example SQL Query

Once data is stored in PostgreSQL, it can be queried directly:

```sql
SELECT date, open, close
FROM analytics.stock_prices
WHERE ticker = 'AAPL'
ORDER BY date DESC
LIMIT 10;
```

---

## 📊 Example Output (Console Summary)

```
Mean_price: 103.165304
Volatility: 0.03128
Max_price: 207.028473
Min_price: 14.250734
```

---

## 📈 Example Visualization

Close price with MA20 and MA50:

![Example Plot](assets/plot_example.png)

---

## 🧪 Interactive Exploration

Open:

```
notebooks/exploration.ipynb
```

This notebook allows:

* manual experimentation
* additional metrics
* correlation checks
* exploratory analysis

---

## 🛠 Technologies

* Python 3.9+
* Pandas, NumPy
* PostgreSQL
* SQLAlchemy, psycopg2
* Matplotlib, Seaborn
* yfinance API
* argparse (CLI)
* logging

---

## 🎯 Purpose

This project was built to demonstrate:

* End-to-end data pipeline design
* Automation mindset
* Modular Python architecture
* Practical SQL integration
* Real-world analytics workflow

---

## License

MIT License

```

---