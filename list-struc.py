from itertools import count

my_list = [0,1,2,3,4,5]
name = ["ali" , "farzane" , "sara" , "mohsen" , "dana" , "mehdi" , "alireza" , "taken"]
print(my_list[1:4])
print(len(my_list))
new_list =  my_list + name
new_list_2 = my_list * 3
print(new_list_2)
print(new_list_2.count(5))


last_name = name.pop(1)
print(last_name)

make_it_test = ('-'.join(name))
print(make_it_test)

list = [1, 2, 3, 4, 5]

list.pop(2)
list.append(10)

print(list)


