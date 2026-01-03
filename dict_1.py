'''
Questions:
1- What is dictionary?
2- Why dictionary is used?
3- When to use dictionary?
4- Where to use Dictionary? (Real-World Examples)
5- How Dictionary Works Internally?
6- Benefits of Using Dictionary?
7- Cons of Using Dictionary?
8- When NOT to Use Dictionary?
9- How insertion order is maintained in Python dict (Python 3.7+)
10- Why Dictionary uses MORE memory than list or tuple?
11- Where dictionary is heavily used?
'''

'''1- What is Dictionary? '''
# A dictionary in Python is a data structure that stores data in KEY : VALUE pairs.
# Ex:  
person = {
    "name": "Tushar",
    "age": 31,
    "city": "Indore"
}

# syntax : dictionary = {"key":"value"}

# In above example name is "key" and "Tushar" is value. Keys are unique, immutable but value can be anything and mutable.

'''2- Why dictionary is used?'''
# Dictionary is used when we want :
# 1- Fast access to data.
# 2- Data in meaningful form (not by index)
# 3- Data with relationship


'''3- When to use dictionary?'''
# Condition 1: Data has meaning
student = {
    "roll_no": 101,
    "marks": 85,
    "grade": "A"
}
# Here every value has a label

# Condition 2: Fast lookup is needed
prices = {
    "apple": 100,
    "banana": 40
}

print(prices["apple"])  # Very fast

# Condition 3: Data is dynamic
# user_profile["age"] = 32

'''4- Where to use Dictionary? (Real-World Examples)'''
# 1- REST API Responses (VERY IMPORTANT)
response = {
    "status": 500,
    "message": "Internal Server Error",
    "data": {...}
}

# 2- Banking 
account = {
    "account_no": 12345,
    "balance": 50000,
    "status": "active"
}

# 3- E-Commerce
product = {
    "id": 101,
    "name": "iPhone",
    "price": 80000
}

# 4- Backend (Flask / FastAPI)
request_data = {
    "Enter mobile number or email": "admin",
    "password": "1234"
}

# Examples:
    # User profiles

    # Config files

    # JSON APIs

    # Counters

    # Caching > To help decreasing access time

    # Database records > 

''' 5- How Dictionary Works Internally?'''
# Python dictionary uses HASHING.
    #What it means:

        #Key → converted into a hash number 

        #Hash → points to memory location

        #Value → stored there

#💡 Result:

# Access time is almost O(1) (very fast)
# That’s why:
account["name"]
# is faster than searching a list.

'''6- Benefits of Using Dictionary? '''
# ⭐ 1. Very Fast : Direct access using key
# ⭐ 2. Easy to Read : user["email"] > is clear than user[3]
# ⭐ 3. Flexible Data Types
        # Keys can be:
            # string ,integer , tuple ( Why can't be list or dict?)
        
        # Values can be:
            # int, str, list, dict, object
# ⭐ 4. Dynamic Size: You can add/remove anytime:
        # user["phone"] = "9999999999"
# ⭐ 5. Perfect for JSON & APIs
        #Python dict ↔ JSON
        #Very important for backend & cloud.

'''7- Cons of Using Dictionary '''
#1. Memory Heavy
    # Dictionary uses more memory than list or tuple.

'''8- When NOT to Use Dictionary?'''
    # If memory is very limited.

    # If you need duplicate keys (dictionary won’t allow)

'''9- How insertion order is maintained in Python dict (Python 3.7+)'''
# Keys stay in the same order in which you insert them
d = {}
d["name"] = "Tushar"
d["age"] = 30
d["city"] = "Indore"

print(d)

#OP: 
# {'name': 'Tushar', 'age': 30, 'city': 'Indore'}

'''10- Why Dictionary uses MORE memory than list or tuple?'''
# Because dictionary stores:

    # Key

    # Value

    # Hash of key

    # Pointer to next element (for collision handling)

    # Empty slots (to keep lookup fast)
'''
    | Data Structure | Stores                       | Memory Usage |
    | -------------- | ---------------------------- | ------------ |
    | List           | Values only                  | Low          |
    | Tuple          | Values only (immutable)      | Lowest       |
    | Dict           | Key + Value + Hash + Pointer | High         |
'''

''' 11- Where dictionary is heavily used?'''
    # REST APIs (JSON)

    # Configuration management (config)

    # Caching systems (Redis-like logic)

    # ML feature mappings

    # Web frameworks (Flask, FastAPI)

    # Airflow DAG configs

''' Interview Definition'''
# Python dictionary is a hash-table based data structure that stores key-value pairs, provides O(1) average lookup time, 
# preserves insertion order from Python 3.7 onwards, and trades higher memory usage for speed and flexibility.
