from load_data import load_student_data,display_student_info

def main():
  file_path="data/raw/student.csv"
  students=load_student_data(file_path)
  if students is not None:
    printf("loaded student dataset sucessfully.")
    display_student_info(stuydents)
  else:
    print("Unable to load student dataset.")

if __name__=="__main__":
  main()
