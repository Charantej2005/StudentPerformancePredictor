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

    students = load_students_data(file_path)

    if students is not None:
        print("Student dataset loaded successfully.")

        # Clean the dataset
        students = remove_duplicates(students)
        check_missing_values(students)
        students = fill_missing_values(students)
        students = validate_marks(students)

        # Analyze the dataset
        dataset_analysis(students)
        missing_values(students)
        unique_value(students)
        numerical_summary(students)

        # Grading the dataset
        students = calculate_total_marks(students)
        students = calculate_average_marks(students)
        students = assign_grade(students)
        students = pass_fail_status(students)

        print("\nUpdated Dataset:")
        print(students.head())

        # Ranking the dataset
        students = generate_rank(students)

        find_topper(students)

        top_five_students(students)
    
        bottom_five_students(students)

        # Report generation
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
