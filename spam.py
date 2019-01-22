def spam1():

    def spam2():

        def spam3():
            z = " even"
            z += y
            print("In spam3, locals are {}".format(locals()))
            return z

        y = " more " + x  # y must exist before spam3 is called
        y += spam3()  # do not combine these assignments
        print("In spam2, locals are {}".format(locals()))
        return y

    x = "spam"  # x must exist before spam2 is called
    x += spam2()  # do not combine these assignments
    print("In spam1, locals are {}".format(locals()))
    return x


print(spam1())
print(locals())
print(globals())

# spam3 originally had a single variable named "z" but when you return
# the program, you can see it also has "y" as local and spam2 gets an
# "x" variable. This enables Python to run faster:
# When you use a nonlocal variable, Python adds it to the local namespace
# so it doesn't have to go hunting through all the enclosing scopes every
# time we use it.
# LEGB - Local, Enclosed, Global, BuiltIn
# Order in which Python looks for your variables.
