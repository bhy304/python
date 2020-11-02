user = {'name': 'alghost', 'email': 'alghost.lee@gmail.com', 'age': 19}

if 'email' in user:
    if '@' not in user['email']:
        print('Wrong Email')
    else:
        print('Email: ' + user['email'])
else:
    print('No email')

teenager = []
if 'age' in user:
    if user['age'] < 20:
        if user['name'] not in teenager:
            print('Name: ' + user['name'])
            teenager.append(user['name'])
        else:
            print('Not teenager')
    else:
        print('No age')

if not teenager:
    print('No teenager')
else:
    print(teenager)