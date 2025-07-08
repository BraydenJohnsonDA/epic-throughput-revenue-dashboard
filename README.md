# Epic Patient Throughput & Revenue Cycle Dashboard

This project was developed by Brayden Johnson as a technical demonstration for the Epic Patient Throughput and Revenue Systems Analyst position at Freeman Health System. It simulates how an Epic analyst supports inpatient operations and revenue performance by identifying workflow delays and billing inefficiencies using mock Epic-like data.

---

## Project Purpose

This dashboard analyzes both patient movement and revenue cycle delays to demonstrate how operational and billing inefficiencies can be surfaced through data. It reflects the dual responsibility of supporting clinical throughput and financial accuracy through Epic.

---

## Key Insights

- **Average Length of Stay (LOS):** 101.6 hours, highest in Ortho, ICU, and Oncology
- **Average Discharge Delay:** 5.9 hours between discharge order and execution
- **Average Time to First Order:** 3.6 hours after admission
- **Average Charge Lag:** 36.8 hours, highest in Oncology and Neuro units
- **Average Payment Lag:** 122.0 hours from charge entry to posted payment
- **Denial Rate:** 26.0%, primarily due to missing documentation and authorization issues

---

## Recommendations

- Automate alerts in Epic for discharge delays over 4 hours
- Standardize and audit charge entry workflows in high-lag units
- Deploy pre-bill checks for missing documentation and prior auth flags
- Launch denial reduction training in Telemetry and Med/Surg units

---

## Files Included

| File Name                                 | Description |
|------------------------------------------|-------------|
| `epic_throughput_revenue_dashboard.pbix` | Power BI dashboard |
| `epic_throughput_revenue_data.csv`       | Mock Epic dataset |
| `generate_epic_throughput_revenue_data.py` | Python script to generate mock data |
| `epic_throughput_revenue_dashboard_screenshot.png` | Visual preview of dashboard |
| `BraydenJohnson_EpicThroughputRevenue_Summary.pdf` | One-page executive summary |

---

## Tools Used

- Power BI
- Python (for mock data generation)
- DAX (for KPIs and measures)
- GitHub (portfolio hosting)

---

## About the Author

I'm Brayden Johnson, a systems-focused data analyst with experience in operational strategy and healthcare workflows. This project is part of my portfolio showcasing how I use Epic-like data to support decision-making in real-world healthcare environments.

