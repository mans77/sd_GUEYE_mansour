#importation de module entree
import tkinterp
import yaml_to_dictio
import json_to_dict
import xml_to_dict
import csv_vers_dict
import pathlib
#importation des modules de sortie
import dict_vers_csv
import dict_to_xml
import dict_to_yaml
import dict_to_json
# validite du fichier d'entree
def  entry_valid(entree_perso):
    if entree_perso.endswith((".csv",".yaml",".xml",".json")):
      
        print("valid")
        return entree_perso
    else:
        print("invalid")
        #print("invalid")
    

# fonction d'entrer d'entree 
def file_enter_dict(entree_perso):

    if entree_perso.endswith(".yaml"):
         return yaml_to_dictio.yaml_to_dict(entree_perso)
    elif entree_perso.endswith(".json"):
         return json_to_dict.json_to_dict(entree_perso)
    elif entree_perso.endswith(".xml"):
         return xml_to_dict.xml_to_dict(entree_perso)
    else:
         return csv_vers_dict.read(entree_perso)
#verification entree utilisateur
def out_valid(entree_perso):
    entree_perso=entry_valid(tkinterp.browse_button())
    while True :
        
        choixutil = str(input("entrer votre extension de sortie:"))
        if pathlib.Path(entree_perso).suffix  == choixutil:
           print("l'extension d'entree correspond a l'extension de sortie veuillez entrer une autre extension")
           
        else:
            return choixutil


def file_to_out(choixutil):
    
    if choixutil== ".yaml":
        return dict_to_yaml.dict_to_yaml(file_enter_dict(entry_valid(tkinterp.browse_button())))
    elif choixutil == ".json":
        return dict_to_json.dict_to_json(file_enter_dict(entry_valid(tkinterp.browse_button())))
    elif choixutil == ".xml":
        return dict_to_xml.DictToXML(file_enter_dict(entry_valid(tkinterp.browse_button()))).display()
    else:
        return dict_vers_csv.dict_to_csv(file_enter_dict(entry_valid(tkinterp.browse_button())))


#entry_valid(tkinterp.browse_button())
#file_enter_dict(entry_valid(tkinterp.browse_button()))
#out_valid(file_enter_dict(entry_valid(tkinterp.browse_button())))
file_to_out(out_valid(file_enter_dict(entry_valid(tkinterp.browse_button()))))