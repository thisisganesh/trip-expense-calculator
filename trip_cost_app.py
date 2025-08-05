# trip_cost_app.py

import streamlit as st
import pandas as pd
import math

st.title("Trip Cost Calculator")

# Input Fields
trip_name = st.text_input("Trip Name")
distance = st.number_input("Distance (in km)", min_value=1.0)
mileage = st.number_input("Car Mileage (km/l)", min_value=1.0)
fuel_price = st.number_input("Fuel Price per Litre (₹)", value=104)
toll_cost_per_km = st.number_input("Toll Cost per Kilometer(₹)", value=3.0)
stay_cost_per_day = st.number_input("Stay Cost per Day (₹)", value=500.0)
food_cost_once = st.number_input("Cost of 1 Meal(₹)", value=200.0)
chai_pani_cost = st.number_input("Misc Cost like Tea / Water(₹)", value=100.0)
no_of_pp = st.number_input("Count of Person(₹)", value=4)

if distance > 0:
    days_estimated = math.ceil(distance / 400)
else:
    days_estimated = 1  # Default

# 🔹 Estimated and Editable Days
estimated_days = math.ceil(distance / 400) if distance > 0 else 1
days_used = st.number_input("Number of Days (estimated, but editable)", min_value=1, value=estimated_days)

# 🔹 Calculations with math.ceil
fuel_required = math.ceil(distance / mileage) if mileage > 0 else 0
fuel_cost = math.ceil(fuel_required * fuel_price)
toll_cost = math.ceil(toll_cost_per_km * distance)
stay_cost = math.ceil(stay_cost_per_day * days_used)
food_cost = math.ceil(((food_cost_once * 2) + chai_pani_cost) * days_used)

total_cost = fuel_cost + toll_cost + stay_cost + food_cost
total_cost_pp = (fuel_cost + toll_cost)/4  + stay_cost + food_cost

# Output
st.subheader("Trip Summary")
st.write(f"Trip Name: **{trip_name}**")
st.write(f"Fuel Needed: **{fuel_required:.2f} litres**")
st.write(f"Fuel Cost: ₹ **{fuel_cost:.2f}**")
st.write(f"Toll Cost: ₹ **{toll_cost:.2f}**")
st.write(f"Stay Cost: ₹ **{stay_cost:.2f}**")
st.write(f"**Total Cost: ₹ {total_cost:.2f}**")
st.write(f"**Per Person Cost: ₹ {total_cost_pp:.2f}**")


# Create a summary DataFrame
summary = pd.DataFrame({
    'Item': ['Fuel Cost', 'Toll Cost', 'Stay Cost', 'Total Cost'],
    'Amount (₹)': [fuel_cost, toll_cost, stay_cost, total_cost]
})

# Export to Excel
st.download_button("Download as Excel", summary.to_csv(index=False), "trip_cost_summary.csv")