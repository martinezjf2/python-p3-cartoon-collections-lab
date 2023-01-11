def roll_call_dwarves(list):
    for index, name in enumerate(list):
        print(f"{index+1}. {name}")
    

def summon_captain_planet(list):
    # Strategy 1: For Loop
    # new_list = []
    # for element in list:
    #     new_element = element[0].upper() + element[1:-1] + "!"
    #     new_list.append(new_element)
    # return new_list

    # Strategy 2: List Comprehension
    new_list = [f"{element[0].upper()}{element[1:]}!" for element in list ]
    return new_list
    pass

# Resource on upper() method: https://www.programiz.com/python-programming/methods/string/upper
# Resource on Slicing Lists : https://www.geeksforgeeks.org/python-list-slicing/


def long_planeteer_calls(list):
    for element in list:
        if len(element) > 4:
            return True
    return False


def find_the_cheese(list):
    cheese = ["cheddar", "gouda", "thyme"]
    for element in list:
        if element in cheese:
            return element
    return None    

# Resource on the "in" keyword: https://www.w3schools.com/python/ref_keyword_in.asp
    
