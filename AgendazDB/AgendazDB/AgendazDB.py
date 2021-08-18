#from Scrollable_frame import Scrollable
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from Constants import *

#0.0 GLOBAL FUNCTIONS
def Cleaner(event, strng):
    strng.set('')
#def button():
   #button = ttk.Button(self.labelFrame, text = "Browse A File",command = fileDialog)
   #button.grid(column = 1, row = 1)
def menu_callback():
    print("I'm in the menu callback!")
    #filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
       # (("jpeg files","*.jpg"),("all files","*.*")) )
    #label = ttk.Label(labelFrame, text = "")
    #label.grid(column = 1, row = 2)
    #label.configure(text = filename)
def submenu_callback():
    print("I'm in the submenu callback!")
    global filename 
    filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
    #f=open(datastrng +".bin","wb")
    f=open(filename,"wb")
    num=[5, 10, 15, 20, 25]
    arr=bytearray(num)
    f.write(arr)
    f.close()
    #f=open(datastrng +".bin","rb")
    f=open(filename,"rb")
    num=list(f.read())
    print (num[0])
    f.close()
    print("I'm in the submenu callback!")
def Save_new_file():
    print("I'm in the submenu callback!")
    f=open(filename,"wb")
    num=[5, 10, 15, 20, 25]
    arr=bytearray(num)
    f.write(arr)
    f.close()
    #f=open(datastrng +".bin","rb")
    f=open(filename,"rb")
    num=list(f.read())
    print (num[0])
    f.close()
    print("I'm in the submenu callback!")

def Salir():
    root.destroy();
#0.5 GLOBAL VARIABLES
datastrng='defaultDB'
#ARRAYS
column_names = ["DNI","Nombre","Apellido","Teléfono","Edad", "Género"] 

#OBJECTS
root =Tk()
sv = StringVar()
menu_widget = Menu(root, background='#000099')
submenu_widget = Menu(menu_widget, tearoff=False)
myLabel1 = Label(root,fg='white', text='', width = 0, bg=mycolor)
myLabel2 = Label(root,fg='white', text='                  ', width = 0, bg=mycolor)
textbox = Entry(root, textvariable= sv)

#1.0 MAIN WINDOW CONFIG
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight())) #FULLSCREEN
#root.geometry('705x500')
root.configure(bg=mycolor)
root.title('AgendazDB')

#2.0 MENUS CONFIG
submenu_widget.add_command(label="Nuevo...",
                           command=submenu_callback)
submenu_widget.add_command(label="Abrir...",
                           command=submenu_callback)
submenu_widget.add_command(label="Guardar.",
                           command=submenu_callback)
submenu_widget.add_command(label="Guardar como...",
                           command=submenu_callback)
submenu_widget.add_command(label="Opciones",
                           command=submenu_callback)
submenu_widget.add_command(label="Salir",
                           command=Salir)
menu_widget.add_cascade(label="Archivo", menu=submenu_widget)
menu_widget.add_command(label="Edición",
                        command=menu_callback)
menu_widget.add_command(label="Ayuda",
                        command=menu_callback)
root.config(menu=menu_widget)

#3.0 TEXT BOX CONFIG
textbox.bind("<1>", lambda eff: Cleaner(eff, sv))
textbox.insert(0,string='Buscar...')

#4.0 Frames
vntana = Frame(root, width=750, height=700)
canvas = Canvas(vntana, width=750, height=700)
scrollbar = Scrollbar(vntana, orient="vertical", command=canvas.yview)
scrollbar2 = Scrollbar(vntana, orient="horizontal", command=canvas.xview)
scrollable_frame = Frame(canvas, width=750, height=700)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set, xscrollcommand=scrollbar2.set)

#GUI SPAWN OBJECTS
textbox.grid(row = 0, column = 5, columnspan=2)
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 0)
vntana.grid(row=2, column=1, columnspan=5)
canvas.grid(row=0,column=0)
scrollbar.grid(row=0,column=1, sticky='ns')
scrollbar2.grid(row=2,column=0, sticky='ew')

#------------------------------------------------------------------------------------------#
#                                       GRID SPAWN                                         #
#------------------------------------------------------------------------------------------#
for j in range(width): #Columns
    b = Button(scrollable_frame, text=column_names[j], width=16, bg=mycolor3,fg='white')
    b.grid(row=0, column=j+1)

for j in range(height+1): #Row
    if j== 0:
         b = Button(scrollable_frame, text='-', width=16, bg=mycolor3,fg='white')
         b.grid(row=j, column=0)
    else:
        b = Button(scrollable_frame, text=str(j), width=16, bg=mycolor3,fg='white')
        b.grid(row=j, column=0)

for i in range(height): #Rows 
    for j in range(width): #Columns
        b = Entry(scrollable_frame, text='', width=20)
        b.grid(row=i+1, column=j+1)

root.mainloop()


