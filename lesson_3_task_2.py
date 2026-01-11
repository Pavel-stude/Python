from smartphone import Smartphone

phone1 = Smartphone("iPhone", "17ProMax.", "+79873000202")
phone2 = Smartphone("Samsung", "A15.", "+79020416095")
phone3 = Smartphone("Redmi", "Note8.", "+79065554505")
phone4 = Smartphone("OnePluse", "G15.", "+79060054505")
phone5 = Smartphone("iPhone", "16Pro.", "+79873085574")

catalog = [phone1, phone2, phone3, phone4, phone5]

for p in catalog:
    print(p.brend_phone, "-", p.model_phone, p.number_phone)