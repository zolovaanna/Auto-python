from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 14 Pro", "+79111234567"))
catalog.append(Smartphone("Samsung", "Galaxy S23 Ultra", "+79221234567"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12 Pro", "+79501234567"))
catalog.append(Smartphone("Google", "Pixel 7 Pro", "+79811234567"))
catalog.append(Smartphone("OnePlus", "11", "+79991234567"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")