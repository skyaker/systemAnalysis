import json
import numpy as np

def build_relation_matrix(ranking, n):
  matrix = np.zeros((n, n), dtype=int)
  for i, group in enumerate(ranking):
    if not isinstance(group, list):
      group = [group]
    for x in group:
      for j in range(i, len(ranking)):
        next_group = ranking[j]
        if not isinstance(next_group, list):
          next_group = [next_group]
        for y in next_group:
          matrix[x-1][y-1] = 1
  return matrix

def find_core_of_conflicts(A_matrix, B_matrix, n):
  conflicts = []
  for i in range(n):
    for j in range(n):
      if i != j:
        if A_matrix[i, j] == 1 and A_matrix[j, i] == 0 and B_matrix[i, j] == 0 and B_matrix[j, i] == 1:
          conflicts.append((i + 1, j + 1))
  return conflicts

def main(json_str1, json_str2):
  try:
    ranking_A = json.loads(json_str1)
    ranking_B = json.loads(json_str2)
  except json.JSONDecodeError as e:
    return f"JSON decoding error: {e}"

  n = max(
    max([max(g) if isinstance(g, list) else g for g in ranking_A]),
    max([max(g) if isinstance(g, list) else g for g in ranking_B])
  )

  A_matrix = build_relation_matrix(ranking_A, n)
  B_matrix = build_relation_matrix(ranking_B, n)

  core_conflicts = find_core_of_conflicts(A_matrix, B_matrix, n)

  return json.dumps(core_conflicts)

json_str1 = '[1, [2, 3], 4, [5, 6, 7], 8, 9, 10]'  # Ранжировка A
json_str2 = '[[1, 2], [3, 4, 5], 6, 7, 9, [8, 10]]'  # Ранжировка B
json_str3 = '[3, [1, 4], 2, 6, [5, 7, 8], [9, 10]]' # Ранжировка C
result = main(json_str1, json_str2)
print(result)  
