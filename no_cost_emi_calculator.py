import streamlit as st

st.set_page_config(page_title="No Cost EMI Checker", layout="centered")

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
if st.button("Calculate"):
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
