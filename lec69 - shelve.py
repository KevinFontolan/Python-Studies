import shelve

# with shelve.open('ShelfText') as fruit:
#     fruit['orange'] = 'a sweet, orange citrus fruit'
#     fruit['apple'] = 'good for making cider'
#     fruit['lemon'] = 'a sour, yellow citrus fruit'
#     fruit['grape'] = 'a small, sweet fruit growing in bunches'
#     fruit['lime'] = 'a sour, green citrus fruit'
#
#     print(fruit['lemon'])
#     print(fruit['grape'])
#
# print(fruit)


fruit = shelve.open("ShelfText")
fruit['orange'] = 'a sweet, orange citrus fruit'
fruit['apple'] = 'good for making cider'
fruit['lemon'] = 'a sour, yellow citrus fruit'
fruit['grape'] = 'a small, sweet fruit growing in bunches'
fruit['lime'] = 'a sour, green citrus fruit'

# print(fruit['lemon'])
# print(fruit['grape'])
#
# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":

    if dict_key == "quit"

    description = fruit.get(
        dict_key, "We don't have a {}".format(shelve_key))
    print(description)

fruit.close()

# ------------- MOTORCYCLE EXAMPLE --------------

# with shelve.open("bike2") as bike:
#     bike["make"] = "Honda"
#     bike["model"] = "250 Dream"
#     bike["colour"] = "Red"
#     bike["engine_size"] = 250
#
#     # del bike['engin_size']
#
#     for key in bike:
#         print(key)
#
# # Shelve is persistent. Even though we fixed the error, the wrong
# # entry is still inside the shell file (engin_size).
#
#     print(bike["engine_size"])
#     print(bike["engin_size"])
#     print(bike["colour"])

# -----------------------------------------------
