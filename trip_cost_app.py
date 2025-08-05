# trip_cost_app.py

import streamlit as st
import pandas as pd

st.title("Trip Cost Calculator")

# Input Fields
trip_name = st.text_input("Trip Name")
distance = st.number_input("Distance (in km)", min_value=0.0)
mileage = st.number_input("Car Mileage (km/l)", min_value=1.0)
fuel_price = st.number_input("Fuel Price per Litre (₹)", value=110.0)
toll_cost = st.number_input("Toll Cost (₹)", value=500.0)
no_of_days = st.number_input("Number of Days", min_value=1)
stay_cost_per_day = st.number_input("Stay Cost per Day (₹)", value=1000.0)

# Calculations
fuel_required = distance / mileage
fuel_cost = fuel_required * fuel_price
stay_cost = stay_cost_per_day * no_of_days
total_cost = fuel_cost + toll_cost + stay_cost

# Output
st.subheader("Trip Summary")
st.write(f"Trip Name: **{trip_name}**")
st.write(f"Fuel Needed: **{fuel_required:.2f} litres**")
st.write(f"Fuel Cost: ₹ **{fuel_cost:.2f}**")
st.write(f"Toll Cost: ₹ **{toll_cost:.2f}**")
st.write(f"Stay Cost: ₹ **{stay_cost:.2f}**")
st.write(f"**Total Cost: ₹ {total_cost:.2f}**")


# Create a summary DataFrame
summary = pd.DataFrame({
    'Item': ['Fuel Cost', 'Toll Cost', 'Stay Cost', 'Total Cost'],
    'Amount (₹)': [fuel_cost, toll_cost, stay_cost, total_cost]
})

# Export to Excel
st.download_button("Download as Excel", summary.to_csv(index=False), "trip_cost_summary.csv")