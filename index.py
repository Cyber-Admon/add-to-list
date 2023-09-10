import time

names = ["ayo", 'ade', 'fola', 'tope']
name = input('what is your name ')

for i in names:
    while name == i:
        print(f'{name} your name is in the list of name')
        break
    # elif type(name) != str
    else:
        names.append(name)
        lenam = len(name)//2
        print(f'your name is being added to the list of names, wait for just {lenam} seconds')
        time.sleep(lenam)
        print(names)
        break
