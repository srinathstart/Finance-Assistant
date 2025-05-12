from fastapi import APIRouter
import requests
from bs4 import BeautifulSoup

router = APIRouter()

@router.get("/get_earnings_filings")
def get_earnings_filings():
    url = "https://finance.yahoo.com/calendar/earnings"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.select("table tbody tr")
    earnings = []
    for row in rows[:5]:
        cols = row.find_all('td')
        earnings.append({
            "ticker": cols[0].text,
            "name": cols[1].text,
            "eps_est": cols[4].text,
            "eps_act": cols[5].text
        })
    return earnings