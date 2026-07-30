import pandas as pd


def load_students_data(file_path):
  """load students datasets from student.csv"""
  try:
    data=pd.read_csv(file_path)
    return data
  except FileNotFoundError:
    print("File not found.Check the file path.")
    return None
    
def display_data_info(data):
  """display basic information form the student dataset"""
  print("\n First 5 student records:")
  print(data.head())
  
  data.info()
  print("\n Stastistical summary")
  print(data.describe())
