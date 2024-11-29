import json

with open('/Users/li6ri9ka/PycharmProjects/pytest/src/new_superheroes.json', 'r') as json_file:
    data = json.load(json_file)
    sorted_superheroes = sorted(data['members'], key=lambda k: k['age'], reverse=True)
    sorted_data  = {
        'members': sorted_superheroes,
    }
    with open('new_superheroes.json', 'w') as new_json_file:
        json.dump(sorted_data, new_json_file, indent=4)

def test_test():
    with open('new_superheroes.json', 'r') as json_file:
        data = json.load(json_file)
        for superhero in data['members']:
            assert superhero['age'] >= 30
