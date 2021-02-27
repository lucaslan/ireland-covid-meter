from covid_cases import process_covid_cases


def main() -> None:

    print(
        "- Ireland's Covid Meter -\n"
        "-----------------------\n"
    )
    process_covid_cases()


if __name__ == "__main__":
    main()