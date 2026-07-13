for every_letter in 'Hello world':
    print(every_letter)

songslist = ['Holy Diver', 'Thunderstruck', 'Rebel Rebel']
for song in songslist:
    if song == 'Holy Diver':
        print(song,' - Dio')
    elif song == 'Thunderstruck':
        print(song,' - AC/DC')
    elif song == 'Rebel Rebel':
        print(song,' - David Bowie')

for i in range(1,10):
    for j in range(1,10):
        print('{} X {} = {}'.format(i,j,i*j))

count = 0
while True:
    print('bitter is brave or Repeat this line !')
    count = count + 1
    if count == 5:
        break
    
password_list = ['******','bitter']
def account_login():
    tries = 3
    while tries > 0:
        password = input('Password:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]

        if password_correct:
            print('Login success!')

        elif password_reset:
            new_password = input('Enter a new password :')
            password_list.append(new_password)
            print('Password has changed successfully!')
            account_login()
        else:
            print('Wrong password contact bitter or invalid input!')
            tries = tries - 1
            print( tries, 'times left')
    else:
        print('Your account has been suspended')

account_login()