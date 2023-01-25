if __name__ == "__main__":
    # define lists
    weight_lb = [150, 155, 145, 148]
    weight_kg = []

    # convert lb / 2.205 = kg
    for x in weight_lb:
        weight_kg.append(round(x/2.205, 2))

    # output
    print(weight_kg)
