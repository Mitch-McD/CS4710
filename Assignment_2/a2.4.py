def unique(sample):
    # cast the list to a set to get unique, then cast back to a list
    return list(set(sample))

if __name__ == "__main__":
    sample = [1,2,3,3,3,3,4,5]

    # call unique, pass sample, and print returned value
    print(unique(sample))