import csv


def dict_to_csv(dicto):
    with open('mycsvfile.csv', 'w') as f:  
        w = csv.DictWriter(f, dicto.keys())
        w.writeheader()
        w.writerow(dicto)
