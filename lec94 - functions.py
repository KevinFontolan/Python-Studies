def python_food():
    width = 80
    text = 'Spam and eggs'
    left_margin = (width - len(text)) // 2
    print(' ' * left_margin, text)


def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ''
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return ' ' * left_margin + text


# with open("centred", mode='w') as centred_file:

# call the function
s1 = centre_text('spam and eggs')
s2 = centre_text('spam, spam and eggs')
s3 = centre_text(12)
s4 = centre_text('spam, spam, spam and eggs')
s5 = centre_text("first", "second", 3, 4, "spam",
                 sep=':')
carlos = input("Enter your text: ")
s6 = centre_text(carlos)

with open("menu", "w") as menu:
    print(s1, file=menu)
    print(s2, file=menu)
    print(s3, file=menu)
    print(s4, file=menu)
    print(s5, file=menu)
    print(s6, file=menu)

print(centre_text("=" + str(12 * 3)))
print((centre_text(sorted(["b", "z", "2", 'a']), s6)))
