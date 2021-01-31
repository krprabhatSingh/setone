def decor(func):
    def inner(name):
        if name == "Priyanka":
            print("Hello", name, "How are you")
        else:
            func(name)

    return inner


def wish(name):
    print("Hello",name,"good morning")

#decorfunction = decor(wish)

wish("Pr555555555555555555555555555555555555555abhat")
wish("Priyanka")
wish("Rohan")
wish("Priyanka")
#decorfunction("Prabhatkumar")