import streamlit as st

def generate_financial_advice(age, gender, avenue, purpose, duration):
    """
    Generates financial advice based on user inputs.
    This function simulates the logic from the original prompt-response generation.
    In a real application, 'data_fin' would likely come from a database or a more complex model.
    For this example, we'll use placeholder values for the investment options and reasons.
    """
    # Placeholder for investment options and reasons. In a real app, this would be dynamic.
    # For simplicity, I'm hardcoding some example values based on the provided output structure.
    # You would integrate your actual financial model here to generate these values.
    investment_options = {
        'Mutual_Funds': 'Based on your profile, Mutual Funds are a good option for diversification and professional management.',
        'Equity_Market': 'Equity Market investments offer high growth potential, suitable for your long-term goals.',
        'Debentures': 'Debentures can provide stable returns with moderate risk.',
        'Government_Bonds': 'Government Bonds are low-risk and provide steady income.',
        'Fixed_Deposits': 'Fixed Deposits offer guaranteed returns and capital safety.',
        'PPF': 'PPF is a tax-efficient, long-term savings option.',
        'Gold': 'Gold can act as a hedge against inflation and market volatility.'
    }

    factors_considered = "Returns, Risk Tolerance, Liquidity"
    objective = "Wealth Creation"
    expected_returns = "10%-15%"
    investment_monitoring = "Quarterly"
    reason_equity = "Capital Appreciation"
    reason_mutual = "Diversification"
    reason_bonds = "Safe Investment"
    reason_fd = "Fixed Returns"
    source = "Financial Advisor"

    response = (
        f"Based on your preferences, here are your investment options:\n"
        f"- Mutual Funds: {investment_options['Mutual_Funds']}\n"
        f"- Equity Market: {investment_options['Equity_Market']}\n"
        f"- Debentures: {investment_options['Debentures']}\n"
        f"- Government Bonds: {investment_options['Government_Bonds']}\n"
        f"- Fixed Deposits: {investment_options['Fixed_Deposits']}\n"
        f"- PPF: {investment_options['PPF']}\n"
        f"- Gold: {investment_options['Gold']}\n"
        f"Factors considered: {factors_considered}\n"
        f"Objective: {objective}\n"
        f"Expected returns: {expected_returns}\n"
        f"Investment monitoring: {investment_monitoring}\n"
        f"Reasons for choices:\n"
        f"- Equity: {reason_equity}\n"
        f"- Mutual Funds: {reason_mutual}\n"
        f"- Bonds: {reason_bonds}\n"
        f"- Fixed Deposits: {reason_fd}\n"
        f"Source of information: {source}\n"
    )
    return response

st.set_page_config(page_title="Financial Advisor", layout="centered")
st.title("Personalized Financial Advisor")

st.markdown("Enter your details below to get personalized investment advice.")

# Input fields
with st.form("financial_form"):
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    avenue = st.selectbox("Investment Avenue", ["Mutual Fund", "Equity", "Debentures", "Government Bonds", "Fixed Deposits", "PPF", "Gold"])
    purpose = st.selectbox("Purpose", ["Wealth Creation", "Income", "Tax Saving", "Retirement Planning"])
    duration = st.selectbox("Investment Duration", ["Less than 1 year", "1-3 years", "3-5 years", "More than 5 years"])

    submitted = st.form_submit_button("Get Advice")

    if submitted:
        st.subheader("Your Personalized Investment Advice:")
        advice = generate_financial_advice(age, gender, avenue, purpose, duration)
        st.write(advice)

st.markdown("---")
st.info("Disclaimer: This is a simulated financial advice application for demonstration purposes only. Consult a professional financial advisor for real investment decisions.")