print('Ведите три целых числа') # не смог удержаться :)
first = int(input())
second = int(input())
third = int(input())
# Вариант 1 - правильный
print('Равных среди них: ')
if first == second == third :
    print (3)
elif first != second != third != first:
    print (0)
else:
    print(2)

# Вариант 2 - так тоже работает, но в задании просили избегать or,and,not/ сделал для себя.
#if first == second and second == third and third == first :
#    print (3)
#elif first == second or second == third or third == first :
#    print (2)
#else:
#    print (0)
