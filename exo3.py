red_object = {"apple", "crab", "rose", "strawberry"}
fruits = {"orange", "apple", "strawberry", "grape", "kiwi", "mandarin"}
orange_objects = {"basketball", "fanta", "orange", "autumn leaves", "mandarin"}
if len(red_object.symmetric_difference(fruits)) == 0:
    print("both sets are equal")
else:
   print("sets are not equal")

set_1 = red_object & fruits
print(set_1)

set_2 = red_object - fruits
print(set_2)

set_3 = red_object.union(orange_objects)
print(set_3)

lst = list(set_3.union(fruits))
print(lst)