import streamlit as st
import requests

st.title("📈 Morning Market Brief Assistant")

if st.button("Get Market Brief"):
    market = requests.get("http://localhost:8000/get_asia_tech_data").json()
    earnings = requests.get("http://localhost:8000/get_earnings_filings").json()
    narrative = requests.post("http://localhost:8000/generate_narrative", json={"market": market, "earnings": earnings}).json()
    st.text(narrative["narrative"])
