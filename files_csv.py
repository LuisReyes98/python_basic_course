import csv
import os

FILE_NAME = "file.csv"
FILE_HEADERS = ['name','age']

data = []

def reader():
  global data
  with open(FILE_NAME, mode='r') as f:
    reader = csv.DictReader(f, fieldnames=FILE_HEADERS)
    for row in reader:
      data.append(row)

def writer():
  global data

  tmp_file = '{}.tmp'.format(FILE_NAME)
  with open(tmp_file,mode = 'w') as f:
    writer = csv.DictWriter(f, fieldnames=FILE_HEADERS)
    writer.writerows(data)  
    os.remove(FILE_NAME)
    os.rename(tmp_file, FILE_NAME)


if __name__ == '__main__':
  reader()
  data.append({
    'name': 'juan',
    'age': 29,    
  })
  writer()


