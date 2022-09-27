# Ireland covid meter

## Table of Contents
- [Ireland covid meter](#ireland-covid-meter)
  - [Table of Contents](#table-of-contents)
  - [About The Project](#about-the-project)
  - [Built With](#built-with)
  - [How to setup](#how-to-setup)
  - [License](#license)

## About The Project
`ireland-covid-meter` is a script to keep track of the amount of covid cases across the Republic of Ireland!
It uses the `CovidStatisticsProfileHPSCIrelandOpenData` dataset and Pandas to present it.

## Built With
* Python 3.7
* bash
* love


## How to setup

1. Clone the repo
    ```bash
    git clone **repo link here**
    ```
2. Create a virtual environment
    ```bash
    python3 -m venv .venv
    ```
3. Source the virtual environment and install the project's requirements if required
    ```bash
    source .venv/vin/activate
    ```
    ```bash
    if [[ -f requirements.txt ]]; then pip3 install -r requirements
    ```
3. Run the project
    ```bash
    python3 Covid_meter.py
    ```


## License
Distributed under the MIT License. See `LICENSE` for more information.

