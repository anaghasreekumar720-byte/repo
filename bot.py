import requests
from datetime import date

def get_quote():
    try:
        url = "https://zenquotes.io/api/random"
        response = requests.get(url, timeout=10)

        data = response.json()

        quote = data[0]["q"]
        author = data[0]["a"]

        return f'"{quote}" - {author}'

    except Exception as e:
        return f"Quote unavailable ({e})"


def build_summary():

    today = date.today().strftime("%d-%m-%Y")

    quote = get_quote()

    summary = f"""
=========================
DAILY SUMMARY
{today}
=========================

TODAY'S QUOTE

{quote}

=========================
"""

    return summary


def run():

    summary = build_summary()

    print(summary)

    with open("daily_summary.txt", "w", encoding="utf-8") as file:
        file.write(summary)

    print("Summary saved successfully")


if __name__ == "__main__":
    run()
