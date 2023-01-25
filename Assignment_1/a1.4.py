if __name__ == "__main__":

    # define sets
    it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    A = {19, 22, 24, 20, 25, 26}
    B = {19, 22, 20, 25, 26, 24, 28, 27}
    age = [22, 19, 24, 25, 26, 24, 25, 24]

    print("IT Companies Length:", len(it_companies))  # get length of it companies

    it_companies.add("Twitter")  # add Twitter

    it_companies.update({"Cerner", "Honeywell"})  # add Cerner and Honeywell at the same time

    it_companies.remove("Facebook")  # Remove Facebook

    print("IT Companies:", it_companies)  # print set

    # Difference between Remove and Discard:
    # Remove throws an error if the given set object is not in the set.
    # Discard does NOT through an error if the given set object is not in the set.

    print("\nJoined:", A.union(B),  # join A and B
          "\nIntersection:", A.intersection(B),  # intersect A and B
          "\nIs A subset of B?", A.issubset(B),  # is A subset of B
          "\nAre A and B disjoint sets?", A.isdisjoint(B),  # are A and B disjoint
          "\nJoined A and B, B and A:", A.union(B), B.union(A),  # join A and B, B and A
          "\nSymmetric Difference:", A.symmetric_difference(B))  # symmetric difference of A and B

    # Delete sets
    A.clear()
    B.clear()

    print("\nAge list:", age,
          "\nAge set", set(age),  # cast to set
          "\nList vs Set length - List:", len(age), "Set:", len(set(age)))  # compare lengths

