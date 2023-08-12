#!/usr/bin/python3
if __name__ == '__main__':
    import inspect

    needed_functions = []

    """
    predicate function
    def predicate(name, obj):
        return callable (obj) and name[0] != '_'
    """

    for name, obj in inspect.getmembers(__import__('hidden_4')):
        if name[0] != '_':
            needed_functions.append((name, obj))

    for name, obj in needed_functions:
        print(name)
