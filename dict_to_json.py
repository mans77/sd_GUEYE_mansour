import json 

def dict_to_json(filename):
    with open("test_json.json", "w") as outfile:
        json.dump(filename, outfile, indent=4, sort_keys=False)
        
    
