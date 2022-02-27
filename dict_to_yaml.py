
import json
import yaml
def dict_to_yaml(output_data):
    output_data = eval(json.dumps(output_data)) 
    ff = open('meta.yaml', 'w+')
    yaml.dump(output_data, ff, allow_unicode=True)
