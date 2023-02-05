if __name__ == "__main__":
    #define list
    list = [10,20,30,40,50,60,70,80,90,100]

    # iterate through list length
    for i in range(0,len(list)):
        # grab all odd indexes of list and output
        if i % 2 == 1:
            print(list[i])