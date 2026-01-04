a = input("Введите номер месяца: ")
b = int(a)
def month_to_season(b):
    if b == 12 or b < 3:
        print ("Зима")
    elif 3 <= b <= 5:
        print("Весна")
    elif 6 <= b <= 8:
        print("Лето")
    else:
        print ("Осень")

month_to_season(b)