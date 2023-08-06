import wget


def download(nth: int):
    suffix: str = (
        "st"
        if nth % 10 == 1
        else "nd"
        if nth % 10 == 2
        else "rd"
        if nth % 10 == 3
        else "th"
    )
    url = f"https://github.com/anzhi0708/yeongnok/raw/main/{nth}{suffix}_20220706-000000.csv"
    wget.download(url)
