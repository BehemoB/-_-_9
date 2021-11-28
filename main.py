def sort_sentence(sentence): #cоздаем функцию
    avavavava = sentence.lower() #делаем всю строку строчными буквами
    ououououo = avavavava.split() #делаем список, чтобы было удобнее работать

    def sorting_again(ououououo): #новая функция для сортировки
        return len(ououououo)

    ououououo.sort(key=sorting_again) #сортируем по возрастанию с ключом по функции
    ykykykyky = ' '.join(ououououo) #из списка в строку
    enenenene = ykykykyky.capitalize() #делаем большую букву в начале
    print(enenenene) #мы молодцы
    
sort_sentence(sentence)
