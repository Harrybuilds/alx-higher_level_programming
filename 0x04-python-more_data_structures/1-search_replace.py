#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []

    arguments = [my_list, search, replace]
    if all(arguments) is not None:
        for i in my_list:
            if i != search:
                new_list.append(i)
            else:
                new_list.append(replace)
        return new_list
