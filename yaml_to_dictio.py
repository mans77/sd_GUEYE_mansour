#import tkinterp
import yaml
def yaml_to_dict(filename):
    with open(filename) as f:
        dicto = yaml.full_load(f)
        print(dicto)
#yaml_to_dict(tkinterp.browse_button())