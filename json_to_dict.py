#import tkinterp  
import json 
def json_to_dict(filename):  
    with open(filename) as json_file: 
        data = json.load(json_file) 
        print(data)
#json_to_dict(tkinterp.browse_button())