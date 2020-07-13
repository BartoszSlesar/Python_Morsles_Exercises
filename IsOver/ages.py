import datetime as dt
from fractions import Fraction
TODAY = dt.datetime.now().date()
LEAP_YEAR = 366 if (TODAY.year/4)%2==0 else 365
def get_age(birthday,*,exact=False):
    age = dt.datetime.strptime(birthday, "%Y-%m-%d").date()
    dif = (TODAY.month,TODAY.day)<(age.month,age.day)
    current_age = TODAY.year - age.year - dif
    try:
        age_current_date = age.replace(year= age.year+current_age)
    except:
        age_current_date = age.replace(day=age.day-1,year=age.year+current_age)     
    if age_current_date>TODAY:
        difer_age = ((age_current_date-TODAY).days)
        current_age = (current_age)+Fraction(difer_age,LEAP_YEAR)
    else:
        difer_age = (TODAY-age_current_date).days 
        current_age = current_age+Fraction(difer_age,LEAP_YEAR)
    return current_age if exact else int(current_age)

def is_over(age, birthday):
    birthday = dt.datetime.strptime(birthday, "%Y-%m-%d").date()
    try:
        age_date = birthday.replace(year = birthday.year+age)
    except ValueError:
        age_date = birthday + dt.timedelta(age*365)
    return age_date<=TODAY

