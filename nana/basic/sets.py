my_set = {"january", "February", "march"}
for element in my_set:
    print(element)

my_set.add("April")
print(my_set)
my_set.remove("january")
print(my_set)

my_list = ["january", "February", "march", "january"]
my_list.remove("january")
print(my_list)