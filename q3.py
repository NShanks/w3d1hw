# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]


convert = lambda x: (x[0], (9/5)*x[1] + 32)

print(list(map(convert, places)))