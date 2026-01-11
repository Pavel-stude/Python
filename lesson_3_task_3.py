from address import Address
from mailing import Mailing

from_address = Address("117437", "Moscow", "Mikluho-Maklaya", "90", "22")

to_address = Address("410012", "Saratov", "Tarhova", "3", "21")

mail = Mailing(to_address, from_address, 523, "132456788546")

print("Отправление", mail.track,"из", mail.from_address.index_city + ",",mail.from_address.city + ",",
    mail.from_address.street + ",", mail.from_address.house, "-", mail.from_address.flat,
    "в", mail.to_address.index_city + ",",mail.to_address.city + ",",
    mail.to_address.street + ",",mail.to_address.house, "-", mail.to_address.flat + ".",
    "Стоимость", mail.cost, "рублей.")
