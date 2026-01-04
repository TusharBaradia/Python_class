''' Dict Methods
Method	Description '''
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary


'''1- Method to create dict'''
dict()
#Creates dictionary

d = dict(a=1, b=2)
'''2- Method returns the number of keys'''
len()

#Returns number of keys

len(d)

'''3- Returns all keys'''
keys()
d.keys()

#👉 Output type: dict_keys

'''4- Returns all values'''
values()
d.values()

'''5- Returns key-value pairs'''
items()
d.items()

#Used heavily in loops:
for k, v in d.items():
    print(k, v)

'''6- Safely get value''''
#get(key, default=None)

d.get("age", 0)


#✔ No error if key missing
#❌ d["age"] raises KeyError

'''7- Gets value if exists
Else inserts key with default value
'''
#setdefault(key, default)

d.setdefault("country", "India")

#Used for grouping, counters

'''8- Adds or updates multiple items'''
#update()

d.update({"age": 31, "city": "Indore"})

'''9-Removes key and returns value'''
#pop(key)

d.pop("age")

❌ Error if key not found

'''10-Removes last inserted item (LIFO) '''
popitem()

d.popitem()

#Python 3.7+ behavior relies on insertion order

'''11-Deletes key'''
#del

del d["city"]

'''12-Removes all items'''
#clear()
d.clear()

'''13- Shallow copy'''
#copy()
new_d = d.copy()

'''14-Creates dictionary with same value '''
#fromkeys(iterable, value)


keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)


# ⚠️ Dangerous with mutable values:

dict.fromkeys(keys, [])

'''15-Check key existence '''
#in keyword
"age" in d

'''16-Dictionary comprehension ''' # very strong to use in code
squares = {x: x*x for x in range(5)}
