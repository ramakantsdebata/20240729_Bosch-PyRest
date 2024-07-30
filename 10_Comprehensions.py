fruits = ["apple", "banana", "cherry", 'dragonfruit', 'grapes', 'kiwi']

basket = []
for fruit in fruits:
    if 'a' in fruit:
        basket.append(fruit)

print(basket)

new_basket = [fruit      for fruit in fruits       if 'a' in fruit]
print(new_basket)

lst =  [fruit                   for fruit in fruits       if 'a' in fruit]
tpl =  tuple(fruit                   for fruit in fruits       if 'a' in fruit)
st1 =  {fruit                   for fruit in fruits       if 'a' in fruit}
dct =  {fruit: len(fruit)       for fruit in fruits       if 'a' in fruit}

gen =  (fruit                   for fruit in fruits       if 'a' in fruit)

print(type(lst), lst)
print(type(tpl), tpl)
print(type(st1), st1)
print(type(dct), dct)
print(type(gen), gen)

# lst1 = [1]; print(type(lst1))
# tp1 = (1); print(type(tp1))

x = 10
# print(dir(int))

attribs = [attrib   for attrib in dir(int)    if attrib.startswith('__') == False] #  and <NotCallable>]
print(attribs)


# class MyType
# {
#     ksdklfsjld
#     int operator()(intx, int y)
#     {

#     }
# };

# obj = MyType();
# obj(1, 2);