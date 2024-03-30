import random
print("добро пожаловать в игру камень ножницы бумага!")
playerScore = 0
botScore = 0
for i in range(3):
    answer = input("Что выберешь?\n").lower()
    if answer.find("камень") != -1:
        answer = "к"
    elif answer.find("ножницы") != -1:
        answer = "н"
    elif answer.find("бумага") != -1 or answer.find("бумагу") != -1:
        answer = "б"
    elif answer.find("ящерица") != -1:
        answer = "я"
    elif answer.find("спок") != -1:
        answer = "с"
    botAnswer = random.choice(["камень", "ножницы", "бумагу","ящерица","спок"])
    print(f"А я выберу {botAnswer}")
    botAnswer = botAnswer[0]
    print(botAnswer)
    if answer == botAnswer:
        print("ничья!")
    elif (answer == "к" and botAnswer == "н") or (answer == "н" and botAnswer == "б") or (answer == "б" and botAnswer == "к") or (answer == "я" and botAnswer == "б") or (answer == "я" and botAnswer == "с") or (answer == "с" and botAnswer == "н") or (answer == "с" and botAnswer == "к") :
        print("ты победил!")
        playerScore += 1
    else:
        print("я победил!")
        botScore += 1

if playerScore == botScore:
    print("ничья по итогам трёх раундов!")
elif playerScore > botScore:
    print("ты победил по итогам трёх раундов")
else:
    print("я победил по итогам трёх раундов") 