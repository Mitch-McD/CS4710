if __name__ == "__main__":
    # define star amount per row, set to 0
    starAmt = 0
    # iterate through rows
    for i in range(1,10):
        # if i below 5, increase staramt, else decrease it
        if i < 6:
            starAmt += 1
        else:
            starAmt -= 1
        # print a * staramt times in a row
        for j in range(1, starAmt+1):
            print("* ", end = "")

        print("")
