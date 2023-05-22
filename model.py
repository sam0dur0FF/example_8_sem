def add_contact(data: str):
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(f'{data}\n')


if __name__ == '__main__':
    add_contact('Hello world')
