def calculate_price(weight):
    if weight > 2000:
        price = 200 * (weight / 1000)
    else:
        price = 250 * (weight / 1000)
    return price

weight = float(input("Введите массу конфет в граммах: "))
price = calculate_price(weight)
print("Цена конфет: %.2f рублей" % price)