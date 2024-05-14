while True:
    print("1. Добавить запись")
    print("2. Выйти")
    
    choice = input("Выберите действие: ")
    
    if choice == '1':
        name = input("Введите Название: ")
        content = input("Введите Содержание: ")
        
        try:
            with open('History/ИсторияДействий', 'a') as h:
                h.write(str(name) + " - Название\n")
                h.write(str(content) + " - Содержание\n\n")
        except Exception as e:
            print("Ошибка при записи в историю: ", e)
        
        try:
            with open('МоеРасписание/' + str(name) + '.txt', 'w') as a:
                a.write("Заметка: \n\n" + str(content))
        except Exception as e:
            print("Ошибка при создании расписания: ", e)
        
        print("Расписание сохранено!")
        
    elif choice == '2':
        print("Программа завершена.")
        break
        
    else:
        print("Неверный выбор. Пожалуйста, выберите 1 или 2.")

    
