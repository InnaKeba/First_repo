#Написати код який буде рахувати вік людини
from datetime import datetime

def calculate_person_age(date_of_birth_str: str) -> int:
    date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d")
    today = datetime.today()

    date_of_birth_this_year = date_of_birth.replace(year = today.year)
    age = today.year - date_of_birth.year
    if(date_of_birth_this_year > today):
        age -= 1
    return age

assert calculate_person_age("2000-01-01") == 25
assert calculate_person_age("2024-06-15") == 0
assert calculate_person_age("2024-06-07") == 1
