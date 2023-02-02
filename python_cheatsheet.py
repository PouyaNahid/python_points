
x = "   pytHon        Codes   is excellent"
print(x.upper())
print(x.lower())
print(x.title())

print(x.strip())
print(f'index of H: {x.find("H")}')
print(x.replace('y', 'i'))
print('t' in x)

# -----------------------------------------------
a = 37
b = 28
if 25 <= b <= 30:
    print ('b is between 25 and 30')
if 20 < a < 30:
    print('a is betewwn 20 and 30')
else:
    print('a is not between 20 and 30')
message = 'a is betewwn 20 and 30' if 20 < a < 30 else 'a is not betewwn 20 and 30'
print(f'message: {message}')

# -----------------------------------------------
def multiple_argument(*arguments):
    for item in arguments:
        print(f'argument: {item}')
multiple_argument(1,'3', 4, 'arg')

def multiple_keyword_arguments(**arguments):

    for item, value in arguments.items():
        print(f'argument: {item} is {value}')

multiple_keyword_arguments(name= 'Pouya', age=37)

# def multiple_ordered_keyword_arguments(arg1, arg2, *args, arg3='shark', **kwargs):
#     print(f'{arg1}\n{arg2}\n{arg3}\n{kwargs}\n{args}')

# # kwargs = {'kwargs_1'="Shark", 'kwargs_2'=4.5, 'kwargs_3'=True}
# multiple_ordered_keyword_arguments(1, 2, 3, 4, 5,'A3', 'A4',('kwargs_1'="Shark", 'kwargs_2'=4.5, 'kwargs_3'=True))

# List ---------------------------------------------
l = [1, 2, 3, 4, 5, 6, 7, 8]
first, second, *o = l
print(first,'--', second)

for indx, value in enumerate(l):
    print(f'{value} is at index :{indx}')
l.append(9)
l.insert(0, 'a')
print(l)

print('pop', l.pop(), '--l:', l)

print('pop(0)', l.pop(0), '--l:', l)
print('remove(5):', l.remove(5), '--l:', l)
del l[0:2]
print('del l[0:2]:', '--l:', l)

if 7 in l:
    print(f'7 index in {l} is: {l.index(7)}')

l = ['a', 'r', 'b', 'g', 'x']
l_sort = sorted(l)
print('l reverse sort:', l_sort, sorted(l, reverse=True))


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
list3 = ['a', 'b', 'c', 'd']
combined = list(zip(list1, list2, list3))
print(combined)
combined = [*list1, 'x', *list2]
print(combined)

matrix = [[0] * 5  for i in range(5)]
print(matrix)

# Tuple ---------------------------------------------
a = tuple()
a += (3,)
print(a)
a += (3,)
print(a)
b = {('a', 'b'): 2, ('c', 'd'): 4}
print(b[('a', 'b')])

# Set ---------------------------------------------
first_set = {1, 2, 3, 4}
second_set = {'a', 'b', 4}
print(first_set | second_set)
print(first_set & second_set)
print(first_set - second_set)
print(first_set ^ second_set)

# Dictionary ---------------------------------------------
dict1 = {'x': 0, 'y': 4}
print(dict1)
dict2 = dict(z = 4, w = 9)
print(dict2)
dict1['t'] = -1
print(dict1)
print(dict2.get('z'))

for key in dict1:
    print(key, dict1[key])

for value in dict1.values():
    print(value)

for key, value in dict1.items():
    print(key, value)

# Comprehensions ---------------------------------------------
values = [x for x in range(10) if x % 2 == 1]       # List
print(type(values), values)

values = {x: x * 2 for x in range(5)}               # Dictionary
print(type(values), values)

values = {x * 2 for x in range(5)}                  # Sets
print(type(values), values)

# ---------------------------------------------
num = [1, 22, 312, 44, 5, 60, 7, 8]
a = []
try:
    for value in num:
        a.append(value * value / (value - 2))
except(ValueError, ZeroDivisionError):
    print('Exception num is:', num)
else:
    print(sorted(a))    # will be run if no exceptions raised
finally:
    print('finished')   # allways run with or without exception

for item in num:
    if item > 30:
        raise ValueError(f'{item} is greater than 30')

# ---------------------------------------------
def generator_func(start, step):
    while True:
        yield start
        start += step

my_gen = generator_func(3, 3)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

# ---------------------------------------------
def square(num):
    return num * num
def is_even(num):
    return num % 2 == 0

b = list(map(square,[1, 3, 5, 6]))
print(b)
c  = list(filter(is_even, [1, 3, 5, 8, 10]))    # return value of is_even must be True or False
print('filter even nums:', c)

# for item in a:
#     print(item())
v1 = [1, 3, 5]
v2 = [10, 20, 30]
print(list(map(lambda x, y: x * y, v1, v2)))

a = [i for i in range(9)]
b = ['x', 'o', '', 'x', 'o', '', '', 'o', 'x']
print(list(zip(a, b)))

print(len(list(filter(lambda i: i == 'o', b))))

words = ['book', 'ruler', 'car', 'supermarket', 'sandwich']
print(sorted(words, key = lambda word: len(word)))


txt = 'Hello Pouya!'
empty_txt = ''
empty_txt = ''.join([char for char in txt])
print(txt,'\n' ,empty_txt)
# --------------------------------------------
d = {'ab':1, 'cd': 2, 'ef': 3}
b = 'ab'
if b in d:
    print(d[b])
else:
    print('no')

# Decorator -----------------------------------
def make_uppercase(func):
    print('uppercase')
    def uppercase(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return uppercase



@make_uppercase
def print_text(txt):
    print('do every things here')
    return txt

print(print_text('hello boy'))


# --------------------------------------------
class MyClass():
    def __init__(self, first_Arg):
        self.first_Arg = first_Arg
        print('initi class')
        
    def method1(self):
        print(f'This is method 1 {self.first_Arg}')
        
        while self.first_Arg
        

a = 23
b = 'first atring'

print(f'{a = } , {b = }','hello' , sep='\n')