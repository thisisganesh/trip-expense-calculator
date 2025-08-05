A working version of the App is Hosted on below URL

https://tig-trip-calculator.streamlit.app/

# 🚗 Trip Cost Calculator (Streamlit App)

A simple web-based tool to calculate your total trip cost based on distance, mileage, fuel price, tolls, and stay costs. Built with Python and Streamlit.

---

## ✨ Features

- Input trip details like distance, mileage, and days
- Auto-calculates:
  - Fuel cost
  - Toll cost
  - Stay cost
  - Total trip cost
- Easy-to-use web interface (mobile + desktop friendly)
- Runs in your browser — no installations needed

---

## 🔧 Inputs

| Field              | Description                         |
|-------------------|-------------------------------------|
| Trip Name          | Custom name for the trip            |
| Distance (km)      | Total distance to be traveled       |
| Car Mileage (km/l) | Your car's mileage                  |
| Fuel Price (₹/l)   | Cost of petrol or diesel            |
| Toll Cost (₹)      | Estimated or known toll charges     |
| Stay Days          | Number of days for stay             |
| Stay Cost/Day (₹)  | Average stay/hotel cost per night   |

---

## 🚀 How to Run Locally

```bash
pip install streamlit
streamlit run trip_cost_app.py
