from Address import Address
from Mailing import Mailing


my_mailing = Mailing()


my_mailing.to_address = Address("607060", "Выкса", "Ленина", "12", "45")
my_mailing.from_address = Address("101000", "Москва", "Мясницкая", "8", "3")


my_mailing.track = "RA876543216RU"
my_mailing.cost = 450


t = my_mailing.to_address
f = my_mailing.from_address
print(
    f"Отправление {my_mailing.track} "
    f"из {f.index}, {f.city}, {f.street}, {f.house} - {f.flat} "
    f"в {t.index}, {t.city}, {t.street}, {t.house} - {t.flat}. "
    f"Стоимость {my_mailing.cost} рублей."
)
