import json

with open('cours copy.json') as f:
  data = json.load(f)




# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data['1']['groupe'])