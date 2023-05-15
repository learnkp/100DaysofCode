Year = int(input("Enter a year: \n"))
Month = int(input("Enter a month: \n"))


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def calculate_days_in_month(month, leapyear_or_not):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leapyear_or_not:
        if month == 2:
            return days_in_month[month-1] + 1
    else:
        return days_in_month[month-1]


leap_or_not = is_leap_year(year=Year)
month_days = calculate_days_in_month(month=Month, leapyear_or_not=leap_or_not)
print(f"Month has {month_days} days")








