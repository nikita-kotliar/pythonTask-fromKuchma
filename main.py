from datetime import date, datetime


def get_birthdays_per_week(users):
    if users == []:
        return list()
        break
    current_date = date.today()
    current_year = current_date.year
    celebrate = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
    for user in users:
        user_date = user['birthday'].replace(year=current_year)
        # check all birthdays in current year
        if timedelta(days=0) <= (user_date - current_date) <= timedelta(days=7):
            if user_date.weekday() == 0 or user_date.weekday() == 5 or user_date.weekday() == 6:
                celebrate['Monday'].append(user['name'])
            elif user_date.weekday() == 1:
                celebrate['Tuesday'].append(user['name'])
            elif user_date.weekday() == 2:
                celebrate['Wednesday'].append(user['name'])
            elif user_date.weekday() == 3:
                celebrate['Thursday'].append(user['name'])
            elif user_date.weekday() == 4:
                celebrate['Friday'].append(user['name'])

        user1_date = user['birthday'].replace(year=current_year + 1)
        # check all birthdays in next year
        if timedelta(days=0) <= (user1_date - current_date) <= timedelta(days=7):
            if user1_date.weekday() == 0 or user1_date.weekday() == 5 or user1_date.weekday() == 6:
                celebrate['Monday'].append(user['name'])
            elif user1_date.weekday() == 1:
                celebrate['Tuesday'].append(user['name'])
            elif user1_date.weekday() == 2:
                celebrate['Wednesday'].append(user['name'])
            elif user1_date.weekday() == 3:
                celebrate['Thursday'].append(user['name'])
            elif user1_date.weekday() == 4:
                celebrate['Friday'].append(user['name'])

    return celebrate


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
