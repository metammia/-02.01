import random
timeList =["Сегодня", "Завтра", "Очень скоро"]
eventList = ["вы встретите", "с вами случится", "вы найдёте"]
objectList = ["что-то волшебное", "необычный инцидент", "большой сюрприз"]
while True:
 input("введите знак Зодиака")
 time = timeList[random.randint(0, len(timeList) - 1)]
 event = eventList[random.randint(0, len(eventList) - 1)]
 object = objectList[random.randint(0, len(objectList) -
1)]
 print(time + " " + event + " " + object)
 next = input("хотите попробовать ещё раз?")
 if next.lower() != "да" or next.lower() != "yes":
 break
print("Приходите ещё за новыми предсказаниями!")
