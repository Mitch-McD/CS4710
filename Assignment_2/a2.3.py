
def get_types(x):
    # define types array
    types = []

    # for every element in x, append its type to types
    for i in x:
        types.append(type(i))

    # return the list
    return types


if __name__ == "__main__":
    x = [23, "Python", 23.98]
    # call get_types, pass x, and print returned value(s)
    print(get_types(x))