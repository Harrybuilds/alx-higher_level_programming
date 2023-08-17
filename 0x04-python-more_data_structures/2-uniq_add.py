#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list is not None:
        num_tracker = []
        total = 0

        """
        use list comprehension to
        append unique numbers to
        num_tracker list

        option2. typecast list to a set
        the sum up all values
        """
        [num_tracker.append(i) for i in
         my_list if i not in num_tracker]

        for i in num_tracker:
            total += i

        return total
