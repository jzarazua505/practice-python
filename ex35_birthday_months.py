from ex34_birthday_json import get_birthdays

def get_month_name(date):
    months = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    return months[date[:2]]

if __name__ == "__main__":
    birthdays = get_birthdays()
    month_counts = {}
    for birthday in birthdays.values():
        month_name = get_month_name(birthday)
        if month_name not in month_counts:
            month_counts[month_name] = 0
        month_counts[month_name] += 1
    print(month_counts)
