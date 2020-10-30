import datetime


def reformat_date_str(date_str, date_format="%Y-%m-%d",
                      target_date_format="%b %d, %Y"):
    return datetime.datetime.strptime(
        date_str, date_format).strftime(target_date_format)


if __name__ == "__main__":
    print(reformat_date_str("2020-11-02"))
