import streamlit as st
from datetime import datetime

# Title of the dashboard
st.title("Prevailing Interest Calculator for High Yield Savings Plus Accounts")

# Description
st.write("""
This calculator estimates the interest earned based on deposit balance amount in a High Yield Savings Plus Account over a specified period of time. 
Interest rates are as follows:
- **First $50,000**: 1.5% p.a.
- **Next $25,000**: 1.6% p.a.
- **Next $25,000**: 1.8% p.a.
- **Amount > $100,000**: 2.0% p.a.
""")

# User Inputs
balance = st.number_input("Enter the balance amount in the savings account (in $):", min_value=0.0, step=100.0, format="%.2f")
start_date = st.date_input("Select the start date:")
end_date = st.date_input("Select the end date:")

# Ensure valid dates
if start_date > end_date:
    st.error("Start date must be before or equal to the end date.")
else:
    # Calculate the total number of days
    days = (end_date - start_date).days

    # Interest calculation function
    def calculate_interest(balance, days):
        interest = 0.0
        annual_days = 365  # Number of days in a year
        
        # First $50,000 at 1.5% p.a.
        if balance > 0:
            tier_amount = min(balance, 50000)
            interest += tier_amount * 0.015 * days / annual_days
            balance -= tier_amount
        
        # Next $25,000 at 1.6% p.a.
        if balance > 0:
            tier_amount = min(balance, 25000)
            interest += tier_amount * 0.016 * days / annual_days
            balance -= tier_amount
        
        # Next $25,000 at 1.8% p.a.
        if balance > 0:
            tier_amount = min(balance, 25000)
            interest += tier_amount * 0.018 * days / annual_days
            balance -= tier_amount
        
        # Amount > $100,000 at 2.0% p.a.
        if balance > 0:
            interest += balance * 0.02 * days / annual_days
        
        return interest

    # Calculate interest
    interest_earned = calculate_interest(balance, days)

    # Display results
    st.subheader("Results")
    st.write(f"Total number of days: {days}")
    st.write(f"Interest earned: ${interest_earned:,.2f}")