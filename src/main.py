from load_data import load_students_data,display_data_info
from clean_data import(remove_duplicates,check_missing_values,fill_missing_values,validate_marks)

def main():
  file_path="data/raw/students.csv"
  students=load_students_data(file_path)
  
  if students is not None:
    printf("loaded student dataset sucessfully.")
    
    """
    from the line 15 to 18 ,code is written to  clean students data using the clean_data functions.
    """
    
    students=remove_duplicates(students)
    check_missing_values(students)
    students=fill_missing_value(students)
    students=validate_marks(students)
    
    display_data_info(students)
    
  else:
    print("Unable to load student dataset.")

if __name__=="__main__":
  main()
