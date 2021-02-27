from datetime import datetime
from helpers import get_date_range, get_data
import json
import pandas

# CONSTANTS
BASE_URL = (
    "https://services1.arcgis.com/eNO7HHeQ3rUcBllm/arcgis/rest/services/CovidStatisticsProfile"
    "HPSCIrelandOpenData/FeatureServer/0/"
)
DAYS_PRIOR_TODAY = 2
DAYS_PRIOR_TODAY += 1

def build_request(today_date: datetime, start_date: datetime) -> str:
    base_query = (
        f"query?where=Date%20%3E%3D%20TIMESTAMP%20'{start_date}%2000%3A00%3A00'%20AND%20Date%20%3C%"
        f"3D%20TIMESTAMP%20'{today_date}%2000%3A00%3A00'&outFields=Date,ConfirmedCovidCases,TotalCon"
        "firmedCovidCases,ConfirmedCovidDeaths,TotalCovidDeaths,StatisticsProfileDate,CovidCases"
        "Confirmed&returnGeometry=false&outSR=4326&f=json"
    )

    return f"{BASE_URL}{base_query}"


def process_cases_data(raw_data: str) -> list:
    """Return last covid info

    Args:
        raw_data (str): Covid API return
        days (int): amount of

    Returns:
        list: last covid data
    """

    try:
        last_covid_data = json.loads(raw_data)
        last_covid_data = last_covid_data["features"]
        last_covid_data = [ x.get("attributes") for x in last_covid_data]
        return last_covid_data
    except BaseException as e:
        print(f"The following error happened: {e}")
        exit(1)


# create datasets
def build_datasets(processed_data: list) -> pandas.DataFrame:
    df = pandas.DataFrame(processed_data)

    df['Date'] = pandas.to_datetime(df['Date'], unit='ms')
    del df['StatisticsProfileDate']
    del df['CovidCasesConfirmed']
    df.sort_values(by=['Date'], inplace=True, ascending=False)

    return df.to_string(index=False)


def process_covid_cases():

    today_date, start_date = get_date_range(DAYS_PRIOR_TODAY)
    raw_data = get_data(build_request(today_date, start_date))
    process_cases = process_cases_data(raw_data)
    result = build_datasets(process_cases)
    print(result)
