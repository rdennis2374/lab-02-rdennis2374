# Ryan Dennis
# UWYO COSC 1010
# 11/5/2024
# Lab Section: 14
# Sources, people worked with, help given to: Stack Overflow, Geeks for Geeks
# your
# comments
# here

leap = [31,29,31,30,31,30,31,31,30,31,30,31]
normal_year = [31,28,31,30,31,30,31,31,30,31,30,31]
days_of_week = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
normal_dict = {1: 31,2: 28,3: 31,4: 30,5: 31,6: 30,7: 31,8: 31,9: 30,10: 31,11: 30,12: 31}
leap_year_days = {1: 31,2: 29,3: 31,4: 30,5: 31,6: 30,7: 31,8: 31,9: 30,10: 31,11: 30,12: 31}

def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

def jan_week(year):
    y = year -1
    day = (36 + y +(y//4) - (y//100) + (y//400))%7
    return day

def get_week_day():
    date = input("Enter the date in the form XX/XX/XXXX")
    month_day_year = date.split("/")
    month = int(month_day_year[0])
    day = int(month_day_year[1])
    year = int(month_day_year[2])
    if month < 1 or month > 12:
        print("Please input a valid month.")
        return
    elif leap_year(year):
        check = leap_year_days.get(month)
        if check < day:
            print("Please put in a valid date.")
            return
    else:
        check = normal_dict.get(month)
        if check < day:
            print("Please input a valid date.")
            return
    day_of_week(month, day, year)

def day_of_week(month, day, year):
    if leap_year(year):
        days = sum(leap[0:month-1])+day-1
        week_day = (jan_week(year) + days) % 7
        print(days_of_week[week_day])
    else:
        days = sum(normal_year[0:month-1])+day-1
        week_day = (jan_week(year) + days) % 7
        print(days_of_week[week_day])

get_week_day()