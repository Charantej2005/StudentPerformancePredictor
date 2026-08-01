import pandas as pd


def calculate_total_marks(data):
    """Calculates total marks of each student."""

    subjects = [
        "Maths",
        "Physics",
        "Chemistry",
        "English",
        "Computer_Science"
    ]

    data["Total"] = data[subjects].sum(axis=1)

    print("Calculated total marks successfully.\n")

    return data


def calculate_average_marks(data):
    """Calculates average marks of each student."""

    data["Average"] = (data["Total"] / 5).round(2)

    print("Calculated average marks successfully.\n")

    return data


def assign_grade(data):
    """Assign grade based on average marks."""

    grades = []

    for average in data["Average"]:

        if average >= 90:
            grades.append("A+")

        elif average >= 80:
            grades.append("A")

        elif average >= 70:
            grades.append("B")

        elif average >= 60:
            grades.append("C")

        elif average >= 50:
            grades.append("D")

        elif average >= 35:
            grades.append("E")

        else:
            grades.append("F")

    data["Grade"] = grades

    print("Grades assigned successfully.\n")

    return data


def pass_fail_status(data):
    """Determines pass/fail status."""

    result = []

    for average in data["Average"]:

        if average >= 35:
            result.append("Pass")

        else:
            result.append("Fail")

    data["Result"] = result

    print("Generated pass/fail status successfully.\n")

    return data
