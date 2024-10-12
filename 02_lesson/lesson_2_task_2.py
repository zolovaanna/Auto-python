def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

# Пример вызова функции
selected_year = 2023
result = is_year_leap(selected_year)
print(f"год {selected_year}: {result}")