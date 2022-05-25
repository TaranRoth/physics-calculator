import json

test = {
    "hi":"bye",
}

print(json.loads(json.dumps(test)))