my_dict = {0: 45, 1: 7, 2: 44, 3: 81, 4: 6}
sort = sorted(my_dict.values())
sort1 = sorted(my_dict.keys())
a = dict(zip(sort1, sort))
print(a)


