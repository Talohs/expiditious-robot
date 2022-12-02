def is_leap_year(a_year):
    #prints a boolean statement if a year is a leap year or not
    print(a_year)
    if ((a_year % 4 == 0 and a_year % 100 != 0) or a_year % 400 == 0):
        return True
    else:
        return False