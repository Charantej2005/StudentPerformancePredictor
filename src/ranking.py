import pandas as pd


def generate_rank(data):
    """Generates rank based on total marks."""

    data = data.sort_values(
        by="Total",
        ascending=False
    )

    data["Rank"] = range(1, len(data) + 1)

    print("Ranks generated successfully.\n")

    return data
def find_topper(data):
    """Displays the overall topper."""

    topper = data.loc[data["Total"].idxmax()]

    print("\nOverall Topper")

    print(topper)

    return topper

def top_five_students(data):
    """Displays top five students."""

    print("\nTop Five Students")

    print(data.nlargest(5, "Total"))

    return data

def bottom_five_students(data):
    """Displays bottom five students."""

    print("\nBottom Five Students")

    print(data.nsmallest(5, "Total"))

    return data
