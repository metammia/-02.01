def convert_to_meters(decimeters):
    meters = decimeters / 10
    return meters

decimeters = float(input("Введите количество дециметров: "))
meters = convert_to_meters(decimeters)

print(f"{decimeters} дециметров равно {meters} метров")
