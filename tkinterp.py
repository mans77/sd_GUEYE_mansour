from tkinter import filedialog
from tkinter import Label,Button,Tk,StringVar,mainloop
import os

def get_extension(file):
    basename = os.path.basename(file) 
    return basename
    # os independent
  
    #ext = '.'.join(basename.split('.')[1:])
    #print('.' + ext) 
    

def browse_button():

    global folder_path
    filename = filedialog.askopenfilename(initialdir="/home/mansour-gueye/python_test/projet/")
    folder_path.set(filename)
    #print(filename)
    return get_extension(filename)



root = Tk()
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=1, column=2)
button2 = Button(text="choisir un fichier", command=browse_button)
button2.grid(row=1, column=2)
root.after(10000, root.destroy) 
mainloop()



