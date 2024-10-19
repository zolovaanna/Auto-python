from mailing import Mailing
from address import Address

to_address = Address("191025", "Санкт-Петербург", "Невский проспект", "10", "15")
from_address = Address("123456", "Москва", "Тверская улица", "1", "1")
mailing = Mailing(to_address, from_address, 150, "1234567890")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")