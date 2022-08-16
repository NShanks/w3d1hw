# Write an anonymous function that sorts this list by the last name...
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]


author.sort(key=lambda x: x.split(" ")[-1].lower())
print(author)