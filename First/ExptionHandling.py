while True:
    try:
        age = int(input('what is you age ?'))
        100 / age

        # raise ValueError

    except ValueError:
        print('Please enter numeric age value')
        continue

    except ZeroDivisionError:
        print('age should be greater than zero')
        break

    else:
        print(f'you are {age}')
        break
    finally:
        print("finally")
