from utils import display_title, display_separator, check_file_exists
from load_data import load_students_data, display_data_info
from clean_data import (
    remove_duplicates,
    check_missing_values,
    fill_missing_values,
    validate_marks
)
from analysis import (
    dataset_analysis,
    numerical_summary,
    missing_values,
    unique_value
)
from grading import(
    calculate_total_marks,
    calculate_average_marks,
    assign_grade,
    pass_fail_status
)
from ranking import (
    generate_rank,
    find_topper,
    top_five_students,
    bottom_five_students
)
from report import (
    generate_report,
    save_report,
    display_top_students,
    display_failed_students
)

def main():
    file_path = "data/raw/students.csv"

    if not check_file_exists(file_path):
        return

    students = load_students_data(file_path)
    
    if students is not None:
        display_title("Student Performance Predictor")
        print("Student dataset loaded successfully.")

        # Clean the dataset
        display_separator()
        print("Cleaning Dataset")
        students = remove_duplicates(students)
        check_missing_values(students)
        students = fill_missing_values(students)
        students = validate_marks(students)

        # Analyze the dataset
        display_separator()
        print("Dataset Analysis")
        dataset_analysis(students)
        missing_values(students)
        unique_value(students)
        numerical_summary(students)

        # Grading the dataset
        display_separator()
        print("Grading")
        students = calculate_total_marks(students)
        students = calculate_average_marks(students)
        students = assign_grade(students)
        students = pass_fail_status(students)

        print("\nUpdated Dataset:")
        print(students.head())

        # Ranking the dataset
        display_separator()
        print("Ranking")
        students = generate_rank(students)

        find_topper(students)

        top_five_students(students)
    
        bottom_five_students(students)

        # Report generation
        display_separator()
        print("Report Generation")
        students = generate_report(students)
        display_top_students(students)
        display_failed_students(students)
        save_report(students)

        # Display dataset information
        display_data_info(students)

    else:
        print("Unable to load student dataset.")


if __name__ == "__main__":
    main()
