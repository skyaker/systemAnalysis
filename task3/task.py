import math
import csv

def task(file_path):
  matrix = []
  with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      matrix.append([float(x) for x in row])
  
  n = len(matrix)
  k = len(matrix[0])
  
  entropy = 0.0
  for j in range(k):
    for i in range(n):
      lij = matrix[i][j]
      if lij > 0:
        fraction = lij / (n - 1)
        entropy -= fraction * math.log2(fraction)
  
  return round(entropy, 1)

csv_file_path = 'task3.csv'
result = task(csv_file_path)
print(result)
