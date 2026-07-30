from load_data import load_students_data,display_data_info

def main():
  file_path="data/raw/students.csv"
  students=load_students_data(file_path)
  if students is not None:
    printf("loaded student dataset sucessfully.")
    display_data_info(students)
  else:
    print("Unable to load student dataset.")

if __name__=="__main__":
  main()
