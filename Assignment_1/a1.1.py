if __name__ == "__main__":

    # original list
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    ages.sort()  # list is sorted

    ages.extend([min(ages), max(ages)])  # add min and max to list on the end

    if len(ages) % 2 == 0:  # if even number of objects in list
        median = (ages[len(ages)//2] + ages[len(ages)//2-1])/2  # add two middle values and calculate median
    else:
        median = (ages[len(ages)//2])  # odd list, middle value is median

    avg = sum(ages)/len(ages)  # calculate average of the list

    range = max(ages) - min(ages)  # find the range

    # print stuff
    print("List:", ages,
          "\nMin:", min(ages),
          "\nMax:", max(ages),
          "\nMedian:", median,
          "\nAverage:", avg,
          "\nRange:", range)