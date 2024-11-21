import csv
from collections import defaultdict

def task(csv_str: str):
  child_map = defaultdict(list)
  parent_map = defaultdict(list)

  for line in csv.reader(csv_str.splitlines(), delimiter=','):
    if not line:
      continue

    parent, child = line
    child_map[parent].append(child)
    parent_map[child].append(parent)

    if parent not in parent_map:
      parent_map[parent] = []

    if child not in child_map:
      child_map[child] = []

  root_node = next(node for node in parent_map if not parent_map[node])

  leaf_nodes = [node for node in child_map if not child_map[node]]

  node_relations = {
    node: {
      'r1': set(child_map[node]),
      'r2': set(parent_map[node]),
      'r3': set(),
      'r4': set(),
      'r5': set()
    }
    for node in parent_map
  }

  stack = [root_node]
  while stack:
    current = stack.pop()
    for child in child_map[current]:
      node_relations[child]['r4'].update(node_relations[current]['r2'])
      node_relations[child]['r4'].update(node_relations[current]['r4'])
      node_relations[child]['r5'].update(node_relations[current]['r1'] - {child})
      stack.append(child)

  stack = leaf_nodes[:]
  while stack:
    current = stack.pop()
    for parent in parent_map[current]:
      node_relations[parent]['r3'].update(node_relations[current]['r1'])
      node_relations[parent]['r3'].update(node_relations[current]['r3'])
      if parent not in stack:
        stack.append(parent)

  relations_fields = ('r1', 'r2', 'r3', 'r4', 'r5')
  result = "\n".join([
    ",".join(str(len(node_relations[node][field])) for field in relations_fields)
    for node in sorted(node_relations)
  ]) + '\n'

  return result

if __name__ == '__main__':
  example_input = "1,2\n1,3\n3,4\n3,5\n"
  print(task(example_input))