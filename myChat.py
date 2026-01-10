while True:
    userNumber = input('how number of users: ')
    users = []
    
    for i in range(int(userNumber)):
        user = input('whoAreYou: ')
        users.append(user)

    print('')

    while True:
        for user in users: 
            message = input(f"[{user}]: ")

            with open('chat.txt', 'a', encoding='utf-8') as file:
                file.write(f'{user}: {message}\n')
