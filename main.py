import streamlit as st
import pandas as pd
import math

st.set_page_config(page_title="Finance Tools", layout="centered")

# Sidebar Navigation
st.sidebar.title("🔗 Navigation")
app_choice = st.sidebar.radio("Choose a Tool:", ["No Cost EMI Checker", "Trip Cost Calculator"])

# -----------------------
# APP 1: No Cost EMI Checker
# -----------------------
def no_cost_emi_checker():
    st.title("💰 No Cost EMI Checker")
    st.write("""
    Use this tool to check if your 'No Cost EMI' purchase actually had hidden charges.
    Just enter the original product price and your 12 monthly EMI payments.
    """)

    # Input original price
    product_price = st.number_input("Original Product Price (₹)", min_value=0.0, format="%.2f")

    # Input monthly EMIs
    st.subheader("Enter Monthly EMI Payments")
    months = ["August", "September", "October", "November", "December", "January", "February", "March", "April", "May", "June", "July"]
    emi_inputs = []

    cols = st.columns(3)
    for i, month in enumerate(months):
        with cols[i % 3]:
            emi = st.number_input(f"{month}", min_value=0.0, format="%.2f", key=month)
            emi_inputs.append(emi)

    # Calculate when button is pressed
    if st.button("Calculate", key="emi_calc_btn"):
        total_paid = sum(emi_inputs)
        extra_paid = total_paid - product_price
        percentage_extra = (extra_paid / product_price) * 100 if product_price > 0 else 0

        st.markdown("---")
        st.subheader("🧾 Results")
        st.write(f"**Total Paid Over 12 Months:** ₹{total_paid:,.2f}")
        st.write(f"**Original Product Price:** ₹{product_price:,.2f}")
        st.write(f"**Extra Paid:** ₹{extra_paid:,.2f}")
        st.write(f"**Percentage Extra Paid:** {percentage_extra:.2f}%")

        if extra_paid <= 0:
            st.success("✅ Congratulations! You paid no extra — it's a true No Cost EMI.")
        else:
            st.error("❗ You paid extra despite 'No Cost EMI'.")
            st.info("This often happens due to hidden interest, GST, or lack of discount from the seller.")

# -----------------------
# APP 2: Trip Cost Calculator
# -----------------------
def trip_cost_calculator():
    st.title("🚗 Trip Cost Calculator")

    # Input Fields
    trip_name = st.text_input("Trip Name")
    distance = st.number_input("Distance (in km)", min_value=1)
    mileage = st.number_input("Car Mileage (km/l)", min_value=1)
    fuel_price = st.number_input("Fuel Price per Litre (₹)", value=104)
    toll_cost_per_km = st.number_input("Toll Cost per Kilometer(₹)", value=3)
    stay_cost_per_day = st.number_input("Stay Cost per Day (₹)", value=500)
    food_cost_once = st.number_input("Cost of 1 Meal(₹)", value=200.0)
    chai_pani_cost = st.number_input("Misc Cost like Tea / Water(₹)", value=100)
    no_of_pp = st.number_input("Count of Person(₹)", value=4)

    estimated_days = math.ceil(distance / 400) if distance > 0 else 1
    days_used = st.number_input("Number of Days (estimated, but editable)", min_value=1, value=estimated_days)

    # Calculations
    fuel_required = math.ceil(distance / mileage) if mileage > 0 else 0
    fuel_cost = math.ceil(fuel_required * fuel_price)
    toll_cost = math.ceil(toll_cost_per_km * distance)
    stay_cost = math.ceil(stay_cost_per_day * days_used)
    food_cost = math.ceil(((food_cost_once * 2) + chai_pani_cost) * days_used)

    total_cost = fuel_cost + toll_cost + stay_cost + food_cost
    total_cost_pp = (fuel_cost + toll_cost) / no_of_pp + stay_cost + food_cost

    # Output
    st.subheader("Trip Summary")
    st.write(f"Trip Name: **{trip_name}**")
    st.write(f"Fuel Needed: **{fuel_required:.2f} litres**")
    st.write(f"Fuel Cost: ₹ **{fuel_cost:.2f}**")
    st.write(f"Toll Cost: ₹ **{toll_cost:.2f}**")
    st.write(f"Stay Cost: ₹ **{stay_cost:.2f}**")
    st.write(f"**Total Cost: ₹ {total_cost:.2f}**")
    st.write(f"**Per Person Cost: ₹ {total_cost_pp:.2f}**")

    summary = pd.DataFrame({
        'Item': ['Fuel Cost', 'Toll Cost', 'Stay Cost', 'Total Cost'],
        'Amount (₹)': [fuel_cost, toll_cost, stay_cost, total_cost]
    })

    st.download_button("Download as Excel", summary.to_csv(index=False), "trip_cost_summary.csv")

# -----------------------
# Run selected app
# -----------------------
if app_choice == "No Cost EMI Checker":
    no_cost_emi_checker()
elif app_choice == "Trip Cost Calculator":
    trip_cost_calculator()
