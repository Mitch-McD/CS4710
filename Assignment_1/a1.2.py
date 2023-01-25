if __name__ == "__main__":

    dog = {}  # empty dog dictionary

    # add key/value pairs
    dog["name"] = "Dixie"
    dog["color"] = "Black"
    dog["breed"] = "Shepherd Mix"
    dog["legs"] = 4
    dog["age"] = 4

    print(dog)

    # create student dict
    student = {
        "first_name": "Mitchell",
        "last_name": "McDaniel",
        "gender": "M",
        "age": 20,
        "marital_status": "single",
        "skills": ["Python", "Unity"],
        "country": "US",
        "city": "Warrensburg",
        "address": "1337 Dictionary St."
    }

    print("Student:", student)

    print("Student Length:", len(student))  # length of student
    print("Student Skills Type:", type(student["skills"]))  # skills type

    student["skills"].extend(["C#", "SQL", "OOP"])  # add skills

    print("Student Keys:", list(student.keys()))  # keys of student cast to list (gets rid of "dict_keys") on output
    print("Student Values:", list(student.values()))  # values of student cast to list (gets rid of "dict_values")

