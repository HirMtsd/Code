import json
from jsonschema import validate, ValidationError

with open('Country_schema.json', encoding="utf-8") as file_schema:
    json_schema = json.load(file_schema)

with open('Country_list.json', encoding="utf-8") as file_json:
    json_data = json.load(file_json)

try:
    validate(json_data, json_schema)
except ValidationError as e:
    print(e.message)

print('SCUCCESS')
