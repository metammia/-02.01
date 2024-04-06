counter = 0
answer = input("Столица России?\n")
if answer == "Москва" or answer == "москва":
 counter = counter + 1
 rightCounter = 0
questionsCounter = 0
questions = ["сколько цветов у радуги?", "какой язык 
мы изучаем?"]
rightAnswers = ["7", "python"]
while questionsCounter < len(questions):
 answer = input(questions[questionsCounter])
 if answer.lower() == rightAnswers[questionsCounter]:
 rightCounter += 1
 questionsCounter += 1
print(f"вы набрали баллов: {rightCounter}")
