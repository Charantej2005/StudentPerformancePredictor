import pandas as pd


def remove_duplicates(data):
    """Removes duplicate rows from the dataset."""

    duplicate_count = data.duplicated().sum()
    print(f"Duplicate records found: {duplicate_count}")

    data = data.drop_duplicates()

    print("Removed duplicates successfully.")

    return data


def check_missing_values(data):
    """Displays missing values in each column."""

    print("\nMissing Values:")
    print(data.isnull().sum())


def fill_missing_values(data):
    """Fills missing numeric values using the column mean."""

    numeric_columns = data.select_dtypes(include="number").columns

    for column in numeric_columns:
        data[column] = data[column].fillna(data[column].mean())

    return data


def validate_marks(data):
    """Validates that marks are between 0 and 100."""

    subject_columns = [
        "Maths",
        "Physics",
        "Chemistry",
        "English",
        "Computer_Science"
    ]

    for subject in subject_columns:
        invalid = data[
            (data[subject] < 0) |
            (data[subject] > 100)
        ]

        if len(invalid) > 0:
            print(f"Invalid marks found in {subject}")

    print("\nMarks validation completed.")

    return data
  
