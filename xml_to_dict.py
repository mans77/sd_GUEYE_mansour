import xmltodict
#import tkinterp
def xml_to_dict(filename):
    with open(filename, encoding='utf-8', mode='r') as _file:
        data = _file.read()
        data = xmltodict.parse(data, dict_constructor = dict )
        print(data)
#xml_to_dict(tkinterp.browse_button())