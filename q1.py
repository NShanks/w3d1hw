places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]


def noBlanks(x):
    if x.isspace() == True:
        return False
    elif x == "":
        return False
    else:
        return True
    
newPlaces = list(filter(noBlanks, places))
print(newPlaces)