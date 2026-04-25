#  Weather Data Pipeline (ETL Project)

##  Overview
This project is an automated ETL pipeline that fetches real-time weather data from an API, processes it using Python, stores it in MySQL, and visualizes insights using Power BI.

---

##  Tech Stack
- Python
- MySQL
- Power BI
- OpenWeatherMap API

---

##  Pipeline Flow
1. Fetch weather data from API
2. Clean and structure data
3. Store in MySQL database
4. Visualize in Power BI dashboard

---

##  Features
- Automated data collection (runs every minute/hour)
- Data cleaning and transformation
- MySQL database storage
- Interactive dashboard with trends and KPIs

---


---

##  How to Run

1. Clone repo
2. Install dependencies: pip install -r requirements.txt
3. Create `config.py` and add your API key:
```python
API_KEY = "your_api_key"
CITY = "Mumbai"

