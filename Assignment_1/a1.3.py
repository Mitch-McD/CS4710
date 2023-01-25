if __name__ == "__main__":

    # create brothers/sisters tuples
    brothers = ("Stephen", "Steven", "Stephan")
    sisters = ("Stephany", "Stephanie", "Stefanie")

    siblings = brothers + sisters  # join brothers and sisters into siblings tuple

    print("Sibling count:", len(siblings))  # get sibling count

    family_members = siblings + ("Steve", "Steph")  # add father and mother

    print("Family members:", family_members)
