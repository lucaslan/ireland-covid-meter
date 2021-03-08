import pandas as pd
from helpers import get_data
import ssl

URL = (
    "https://raw.githubusercontent.com/owid/covid-19-data/master/"
    "public/data/vaccinations/country_data/Ireland.csv"
)

csv_raw_data = get_data(URL)

def process_vaccines_data(raw_data: str) -> pandas.DataFrame:
    # csv=pd.read_csv(io.StringIO(raw_data.decode('utf-8')))
    ssl._create_default_https_context = ssl._create_unverified_context
    csv = pd.read_table(URL)
    del csv['location']
    return []

process_vaccines_data(csv_raw_data)