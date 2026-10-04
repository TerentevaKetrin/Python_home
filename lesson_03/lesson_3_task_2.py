from smartphone import Smartphone


catalog = []


catalog.append(Smartphone("Apple", "iPhone 15", "+79001111111"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79004444444"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79007777777"))
catalog.append(Smartphone("Honor", "Pixel 8", "+79002222222"))
catalog.append(Smartphone("Alcatel", "12", "+79005555555"))


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
