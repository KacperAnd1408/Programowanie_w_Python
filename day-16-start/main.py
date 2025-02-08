# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
# timmy = Turtle() #skonstruowanie nowego obiektu timmy
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan4")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight) #atrybut - zmienna
# my_screen.exitonclick() #metoda - funkcja

from prettytable import PrettyTable
table = PrettyTable() #skonstruowanie obiektu table

table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', "Fire"])
table.align = "l"

print(table)




