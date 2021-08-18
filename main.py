def printName():
    name = input('Enter Your Name\n')
    if len(name) < 4:
        print('Please Provide a Valid Name')

    else:
        print(f'Welcome to HNG {name} ')


if __name__ == '__main__':
    printName()
