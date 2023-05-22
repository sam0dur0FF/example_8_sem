import view, model


def start():
    view.greetings()
    while True:
        view.menu()
        answer = input('Введие команду: ')
        if answer == '1':
            view.show()  # вывод контактов

        elif answer == '2':
            data = input('Введите данные контакта через пробел: ')
            model.add_contact(data)  # добавить контакт

        elif answer == '3':
            data = input('Введите данные контакта через пробел: ')
            model.search(data)  # поиск

        elif answer == '4':
            view.bye()
            break

        else:
            model.error()  # ошибка, если введено что-то иное.

if __name__ == '__main__':
    start()
