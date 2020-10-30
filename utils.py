import datetime


def reformat_date_str(date_str, date_format="%Y-%m-%d",
                      target_date_format="%b %d, %Y"):
    formatted_date_str = "-"
    try:
        formatted_date_str = datetime.datetime.strptime(
            date_str, date_format).strftime(target_date_format)
    except Exception as e:
        print(f"Error during date conversion: {e})")
    return formatted_date_str


if __name__ == "__main__":
    print(reformat_date_str("2020-06-05"))
