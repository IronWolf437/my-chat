while True:
    # Get number of users & their names
    try:
        userNumber = int(input('how number of users: '))
    except:
        print('\033[0;31mPlease enter a valid numbe\033[0m')
        continue

    users = []

    for i in range(userNumber):
        user = input('whoAreYou: ')
        users.append(user)


    # Get chat title & create/open chat file
    chatTitle = input('chatTitle: ')
    with open(f'{chatTitle}.txt', 'a', encoding='utf-8') as file:
        file

    print(f'\n=== {chatTitle} ===\n')

    with open(f'{chatTitle}.txt', 'r', encoding='utf-8') as file:
        print(file.read())


    # Chat loop
    while True:
        for user in users: 
            message = input(f"[{user}]: ")

            if message == 'exit':
                exit()
            else:
                with open(f'{chatTitle}.txt', 'a', encoding='utf-8') as file:
                    file.write(f'{user}: {message}\n')
