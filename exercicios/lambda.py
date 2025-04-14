while True:
    try:
        n = int(input("Numero: "))
        b = 2
        c = b / n
    except ZeroDivisionError as error:
        print(error)