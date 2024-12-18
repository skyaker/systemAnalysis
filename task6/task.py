import json

def task(temp_json, heating_json, rules_json, current_temp):
  temp_functions = json.loads(temp_json)['температура']
  heating_functions = json.loads(heating_json)['температура']
  rules = json.loads(rules_json)

  def calculate_membership(value, points):
    for i in range(len(points) - 1):
      x1, y1 = points[i]
      x2, y2 = points[i + 1]
      if x1 <= value <= x2:
        return y1 + (value - x1) * (y2 - y1) / (x2 - x1)
    return 0.0

  temp_membership = {term['id']: calculate_membership(current_temp, term['points']) for term in temp_functions}
  output = {}
  for temp_term, heat_term in rules:
    output[heat_term] = max(output.get(heat_term, 0), temp_membership.get(temp_term, 0))

  aggregated = []
  for heating in heating_functions:
    level = output.get(heating['id'], 0)
    aggregated.extend((x, min(y, level)) for x, y in heating['points'])

  numerator = sum(x * y for x, y in aggregated)
  denominator = sum(y for _, y in aggregated)
  return round(numerator / denominator if denominator != 0 else 0.0, 1)

if __name__ == "__main__":
  with open('функции-принадлежности-температуры.json', 'r', encoding='utf-8') as temp_file:
    temp_json = temp_file.read()
  with open('функции-принадлежности-управление.json', 'r', encoding='utf-8') as heating_file:
    heating_json = heating_file.read()
  with open('функция-отображения.json', 'r', encoding='utf-8') as rules_file:
    rules_json = rules_file.read()

  current_temp = 20.0
  print(task(temp_json, heating_json, rules_json, current_temp))