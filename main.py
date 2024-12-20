from datetime import date, timedelta, datetime

def get_birthdays_per_week(users):
    today = date.today()
    # print(today)
    # дата понеділка
    monday_this_week = today - timedelta(days=today.weekday())
    # дата п'ятниці 
    friday_this_week = monday_this_week + timedelta(days=4)
    # початок наступного тижня
    monday_next_week = monday_this_week + timedelta(days=7)

    birthdays_by_day = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
    }

    for user in users:
        birthday = user["birthday"]
        birthday = birthday.replace(year=today.year)

        # Якщо день народження вже пройшов
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        weekday = birthday.weekday()
        # print(weekday)

        # переносиння на понеділок
        if weekday == 5 or weekday == 6:  
            birthday = birthday + timedelta(days=(7 - weekday))
            weekday = 0  

        # додавання дня
        if monday_this_week <= birthday <= friday_this_week or monday_next_week <= birthday < monday_next_week + timedelta(days=5):
            # print (birthday)
            day_name = list(birthdays_by_day.keys())[weekday]
            birthdays_by_day[day_name].append(user["name"])

    # print ({day: names for day, names in birthdays_by_day.items() if names})
    return {day: names for day, names in birthdays_by_day.items() if names}



if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
