def upper_lower(string):
    # define counters
    upperCount, lowerCount = 0, 0
    # for every character in the string
    for letter in string:
        # if uppercase, add to counter
        if letter.isupper():
            upperCount += 1
        # if lowercase, add to counter
        if letter.islower():
            lowerCount += 1
    # output counters
    print(f"No. of Upper-case characters: {upperCount}\n"
          f"No. of Lower-case characters: {lowerCount}")


if __name__ == "__main__":
    input_string = "The quick Brow Fox"
    # call upper_lower and pass input string
    upper_lower(input_string)