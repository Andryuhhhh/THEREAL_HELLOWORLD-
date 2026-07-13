def helloworld(a):
    try:
        if a == "print":
            print("Hello World!")
        else:
            raise ValueError("Not Hello World!")
    except ValueError:
        print("error")

helloworld("print")