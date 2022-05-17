from datetime import datetime, timedelta

names = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Monday',
    6: 'Monday'
}

def get_birthdays_per_week(college_list: list[dict]) -> None:
    result = {}
    for v in names.values():
        result[v] = []
    now = datetime.now().date()
    dates = []
    dates.append(now)
    for x in range(1, 7):
        dates.append(now + timedelta(days=x))

    for college in college_list:
        for date in dates:
            birthday = college.get('birthday')
            if birthday.day == date.day and birthday.month == date.month:
                result[names[date.weekday()]].append(college.get('name'))

    for k, v in result.items():
        if len(v) == 0:
            continue
        name = ', '.join(v)
        print(f'{k}: {name}')


if __name__ == '__main__':
    college_list =[
        {
            "name": "Alex",
            "birthday": datetime(year=1978, month=5, day=17)
        },
        {
            "name": "Bill",
            "birthday": datetime(year=1999, month=5, day=18)
        },
        {
            "name": "Oleg",
            "birthday": datetime(year=1999, month=5, day=21)
        },
        {
            "name": "Anna",
            "birthday": datetime(year=1999, month=5, day=22)
        },
        {
            "name": "Vlad",
            "birthday": datetime(year=1999, month=6, day=21)
        }
    ]
    get_birthdays_per_week(college_list)





