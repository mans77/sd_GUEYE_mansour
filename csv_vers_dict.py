import csv
#import tkinterp
def read(filename):
    #output = open("data.csv","w")
    with open(filename, 'r') as csvfile:
       
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            #output.write(row)
            print(row)

        
#read(tkinterp.browse_button())

