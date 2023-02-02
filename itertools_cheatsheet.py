# %% [markdown]
# # Table of Contents
# - Map function
# - Filter function
# - Zip function
# 

# %% [markdown]
# # Functions
# ### Map
# 

# %%
l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 11, 12, 13, 14, 15]
def add(x, y):
    return x + y

# %%
# using routine for loop
l3 = []
for i in range(len(l1)):
    l3.append(add(l1[i], l2[i]))
print(l3)

# %%
# using map function in relation to external add() function
l3 = list(map(add, l1, l2))
print(l3)

# %%
# using map function in coordinates with lambda add() function
l3 = list(map(lambda x, y: x + y, l1, l2))
print(l3)

# %% [markdown]
# ### Filter

# %%
l4 = list(filter(lambda x: 10 < x < 18 and x % 2 == 0, l2))
print (l4)

# %% [markdown]
# ### Zip

# %%
l5 = ['dog', 'cat', 'cow', 'lion', 'chicken']
l6 = [10, 11, 12, 13, 14, 15]

d1 = dict(zip(l5, l6))

l7 = list(zip(l5, l6))

s1 =  set(zip(l5, l6))

print(d1, l7, s1, sep='\n')

# %% [markdown]
# #### Quick way to zip dictionaries

# %%
d2 = {'pouya': 1, 'nahid': 2}
d3 = {'age': 37, 'sex': 'male'}

d4 = {**d2, **d3}

print('new dict is:', d4, end='\n')

# %% [markdown]
# ## Itertools Library
# The itertools module is a collection of tools intended to be fast and use memory efficiently when handling iterators (like lists or dictionaries).
# The itertools module comes in the standard library and must be imported.
# The operator module will also be used. This module is not necessary when using itertools, but needed for some of the examples below.

# %%
import itertools
import operator

# %% [markdown]
# ## Count()
# Makes an iterator that returns evenly spaced values starting with number start.
# <br>count(start, step) -> iterator.</br>
# 
# <i>Remember: Each time your generator is called upon using next, it will only then yield the result.
# <br>This will continue until your generator is exhausted.</br></i>

# %%
ctr = itertools.count(start = 10, step = 3)

for i in ctr:
    print(f'{i = }', end= ', ')
    if i > 20:
        break
print(f'\nnext count is {next(ctr)}.')


# %% [markdown]
# ## Cycle()
# This creates an iterable object of what you pass in in an endless cycle.
# <br>cycle(iterable) -> iterator </br>

# %%
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
i = 0
for color in itertools.cycle(colors):
    print(f'{i}: {color}', end= ', ')
    i += 1
    if i > 14:
        break

# %% [markdown]
# 

# %% [markdown]
# ## Repeat()
# This function will repeat an object over and over again. Unless, there is a times argument.
# <br>repeat(object, times)</br>

# %%
list(itertools.repeat('Pouya', 4))

# %%

repeat_object = itertools.repeat('Succed', 4)
print(next(repeat_object))
print(next(repeat_object))
print(next(repeat_object))
print(next(repeat_object))
# print(next(repeat_object))


# %% [markdown]
# ## Accumulate()
# Accumulate makes an iterator that returns accumulated sums.
# <br>accumulate(iterable, func=operator.add) -> iterator </br>

# %%
list(itertools.accumulate([3, 4, 5, 6, 7])) # 3,   3 + 4,   7 (3 + 4) + 5,   12 (3 + 4 + 5) + 6,   19 (3 + 4 + 5 + 6) + 7

# %%
print(operator.mul(3, 5))
print(operator.mul(2, 10))
list(itertools.accumulate([3, 5, 7], operator.mul)) # 3,   3 x 5,    15 (3 x 5) x 7

# %%
def multiply(x, y):
    return x * y * 2
list(itertools.accumulate([3, 5, 7], multiply))

# %%
acc = itertools.accumulate([3, 5, 7])
print(next(acc), end=', ')
print(next(acc), end=', ')
print(next(acc))

# %% [markdown]
# ## Chain()
# Take a series of iterables and return them as one long iterable.
# <br>chain(*iterables) -> iterable </br>
# <i>- Used for treating consecutive sequences as a single sequence.
# <br>- You can chain together lists, tuples, sets and strings</br></i>

# %%
colors = ['red', 'orange', 'yellow', 'green', 'blue']
shapes = ['circle', 'triangle', 'square', 'pentagon']
result = itertools.chain(colors, shapes)
print(result)
print(next(result), end=', ')
print(next(result), end=', ')
print(next(result), end='\n')

for item in result:
    print(item, end=', ')

# %%
s1 = {'pouya', 'nahid'}
l1 = ['age', 'sex']
t1 = ('engineer', 'employeed')

result_dict = itertools.chain(s1, l1, t1, 'IRN')
for item in result_dict:
    print(item, end=', ')

# %% [markdown]
# ## Compress()
# Compress makes an iterator that filters elements from data returning
# only those that have a corresponding element in selectors that
# evaluates to True.
# <br>compress(data, selectors) -> iterator.</br>
# 
# <i>Stops when either the data or selectors iterables have been exhausted.</i>

# %%
list(itertools.compress("ABCDEF", [1, 0, 1, 0, 0, 1]))

# %%
compress_obj = itertools.compress("ABCDEF", [1, 0, 1, 0, 1, 1])

print(next(compress_obj))
print(next(compress_obj))

# %% [markdown]
# ## Dropwhile()
# Make an iterator that drops elements from the iterable as long as the predicate is true; afterwards, returns every element.
# <br>dropwhile(predicate, iterable) -> iterator.</br>

# %%
list(itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# %%
def filter_func(x):
    return True if x < 5 else False

dropwhile_obj = itertools.dropwhile(filter_func, [1, 2, 3, 4, 5, 6, 7, 8])
print(next(dropwhile_obj), end=', ')
print(next(dropwhile_obj), end=', ')
print(next(dropwhile_obj), end=', ')
print(next(dropwhile_obj))

# %% [markdown]
# ## Takewhile()
# Makes an iterator and returns elements from the iterable as long as the predicate is true.The opposite of dropwhile().
# <br>takewhile(predicate, iterable) -> iterator.</br>

# %%
list(itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# %%
def filter_func(x):
    return True if x < 5 else False

dropwhile_obj = itertools.takewhile(filter_func, [1, 2, 3, 4, 5, 6, 7, 8])
print(next(dropwhile_obj), end=', ')
print(next(dropwhile_obj), end=', ')
print(next(dropwhile_obj), end=', ')
print(next(dropwhile_obj))

# %% [markdown]
# ## Filterfalse()
# Makes an iterator that filters elements from iterable returning only those for which the predicate is False.
# <br>filterfalse(predicate, iterable) -> iterator.</br>

# %%
list(itertools.filterfalse(lambda x: x < 4, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# %%
filterfalse_obj = itertools.filterfalse(lambda x: x < 4, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(next(filterfalse_obj), end=', ')
print(next(filterfalse_obj), end=', ')
print(next(filterfalse_obj), end=', ')

# %% [markdown]
# ## Islice()
# This allows you to cut out a piece of an iterable. This function is very much like slices.
# <br>islice(iterable, *args) -> iterator.</br>

# %%
print(list(itertools.islice("ABCDEFGH", 4)))
print(list("ABCDEFGH"[0:4]))

# %%
print(list(itertools.islice("ABCDEFG", 2, 4)))

# similar to

print(list("ABCDEFG"[2:4]))

# %%
print(list(itertools.islice("ABCDEFG", 2, None)))

# similar to

print(list("ABCDEFG"[2:]))

# %%
print(list(itertools.islice("ABCDEFG", 0, None, 3)))

# similar to

print(list("ABCDEFG"[::3]))

# %%
islice_obj = itertools.islice("ABCDEFG", 0, None, 2)
print(next(islice_obj))
print(next(islice_obj))


# %% [markdown]
# ## Starmap()
# Makes an iterator that computes the function using arguments obtained from the iterable.
# <br>starmap(function, iterable) -> iterator.</br>

# %%
print(list(itertools.starmap(pow, [(2, 4), (3, 5), (4, 2)])))

# %%
def any_func(a, b, c):
    return a * b * c

print(list(itertools.starmap(any_func, [(2, 3, 4), (-2, 40, 0), (-2, 4, -3)])))

# %%
starmap_obj = itertools.starmap(operator.mul, [(2, 4), (3, 5), (5, 1)])
print(next(starmap_obj), end = ', ')
print(next(starmap_obj), end = ', ')
print(next(starmap_obj))


# %% [markdown]
# ## Count()
# Makes an iterator that returns evenly spaced values starting with number start.
# <br>count(start, step) -> iterator.</br>
# 
# <i>Remember: Each time your generator is called upon using next, it will only then yield the result.
# <br>This will continue until your generator is exhausted.</br></i>

# %% [markdown]
# ## Count()
# Makes an iterator that returns evenly spaced values starting with number start.
# <br>count(start, step) -> iterator.</br>
# 
# <i>Remember: Each time your generator is called upon using next, it will only then yield the result.
# <br>This will continue until your generator is exhausted.</br></i>

# %% [markdown]
# ## Count()
# Makes an iterator that returns evenly spaced values starting with number start.
# <br>count(start, step) -> iterator.</br>
# 
# <i>Remember: Each time your generator is called upon using next, it will only then yield the result.
# <br>This will continue until your generator is exhausted.</br></i>

# %% [markdown]
# ## Links:
# <br>https://github.com/gpetepg/python_tips</br>
# https://www.pythoncheatsheet.org/modules/itertools-module#filterfalse


