"""
Random Printmuster

"""

for i in range(10):
    randomNumber = random()
    if randomNumber > 0.2:
        print(" *** " + " %%% " + " *** " + " %%% ")
    else:
        print(" %%% " + " *** " + " %%% " + " *** ")