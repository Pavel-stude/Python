years = input("Введите год: ")
years_num = int(years)

def is_year_leap(years_num):
    if years_num % 4 == 0:
        return True
    else:
        return False

result = is_year_leap(years_num)
print("год", years_num, ":", result)
