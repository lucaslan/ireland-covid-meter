import requests
from datetime import datetime, timedelta


def get_date_range(days_prior_today: int) -> str:
    """return date in the string form

    Returns:
        str: today's date in %Y-%m-%d format
    """


    today_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=days_prior_today)).strftime('%Y-%m-%d')

    return today_date, start_date


def get_data(request_url: str) -> str:
    """Get covid data

    Returns:
        str: API resposne
    """

    reponse = requests.get(request_url)
    if reponse.status_code != 200:
        print("Failed to retrieve the data!")
        exit(1)

    return reponse.text


def epoch_to_str(epoch: str) -> str:
    date = int(epoch) / 1000
    converted_date = datetime.fromtimestamp(date)
    return converted_date.strftime('%d-%m-%Y')