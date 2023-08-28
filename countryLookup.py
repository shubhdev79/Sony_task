import json

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

def search_key(json_obj, target_key):
    results = []

    def search_recursive(obj, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    results.append(v)
                elif isinstance(v, (dict, list)):
                    search_recursive(v, key)
        elif isinstance(obj, list):
            for item in obj:
                if isinstance(item, (dict, list)):
                    search_recursive(item, key)

    search_recursive(data, target_key)
    return results

target_key = input('Please provide countrycode: \n')	 # \n ---> newline ---> It causes a line break

search_results = search_key(data, target_key)
print("Country_Name Info:", search_results)
