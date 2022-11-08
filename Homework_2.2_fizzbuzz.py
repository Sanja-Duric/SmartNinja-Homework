i = 1

broj = int(input("Unesi broj od 1 do 100: "))

while i <= broj:

    if i % 5 == 0:
        if i % 3 == 0:
            print("fizzbuzz")
        else:
            print("buzz")

    elif i % 3 == 0:
        print("fizz")

    else:
        print(str(i))
    i += 1

