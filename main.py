from itertools import count
from operator import length_hint

from encodings.aliases import aliases


def main():
    age = 12
    man = "Ali"
    name = ["14.4", "ali", "alireza", "mehdi", "hossein"]
    intager = "0123456789"
    integer = [0, 1, 2, 3, 4, 5]
    string_2 = ["ALIREZA", "MEHDI", "ALI", "SANAZ", "NIMAZAMANI"]
    number = int("123")
    print(type(number))

    print("Hello world")
    print(9 % 2)

    print(name[0:3:2])
    print(integer[::-1])

    for names in name:
        print(names)

    print(integer[::-1])
    print(type(intager))
    print(type(integer))
    print(type(string_2))
    print("Hello my name is %s and my age is %i" % (man, age))


if __name__ == "__main__":
    main()


name = "ali"
family_name = "bagheri"
age = 33

print("hello {} {} you are age are {}".format(name, family_name, age))

f"Hello {name} {family_name}, u are {age:1.1f} years old"

print(len(family_name))
print(name[-1])

x = 'Hi this is a string'

print(x.lower().replace(' ', ','))
print(','.join(x.lower().split()))
print(','.join(x.lower().split()))
