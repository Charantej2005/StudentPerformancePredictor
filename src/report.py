import pandas as pd


def generate_report(data):
    """Displays the complete student performance report."""

    print("\nStudent Performance Report")
    print(data)

    return data


def save_report(data):
    """Saves the student performance report as a CSV file."""

    output_path = "outputs/reports/student_report.csv"

    data.to_csv(output_path, index=False)

    print(f"\nReport saved successfully at {output_path}")

    return output_path


def display_top_students(data):
    """Displays the top 5 ranked students."""

    print("\nTop 5 Students")

    print(data.head(5))


def display_failed_students(data):
    """Displays all failed students."""

    failed_students = data[data["Result"] == "Fail"]

    print("\nFailed Students")

    if failed_students.empty:
        print("No failed students found.")
    else:
        print(failed_students)
