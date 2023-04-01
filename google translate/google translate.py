
from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text_one = text
    src_one = src
    dst_one = dest
    trans = Translator()
    trans_one = trans.translate(text,src=src_one,dest=dst_one)
    return trans_one.text

def data():
    s = sor_comb.get()
    d = sor_comb_dest.get()
    masg = sor_text.get(1.0,END)
    textget = change(text=masg, src=s, dest=d)
    dest_text.delete(1.0,END)
    dest_text.insert(END, textget)



root = Tk()

root.title("Translate")
root.geometry("500x700")
root.config(bg="red")

#############################
label_text = Label(root,text="Google Translate",font=("Time New Roman",20,"bold"))
label_text.place(x=100,y=50,height=50,width=300)

#######################
frame = Frame(root).pack(side=BOTTOM)

label_text = Label(root,text="Sourch Text",font=("Time New Roman",15),bg="red")
label_text.place(x=125,y=110,height=40,width=250)

#############################
sor_text = Text(frame,font=("Time New Roman",20),wrap=WORD)
sor_text.place(x=10,y=180,height=150,width=480)

###################################
list_text = list(LANGUAGES.values())

sor_comb = ttk.Combobox(frame,values=list_text)
sor_comb.place(x=80,y=360,height=30,width=100)
sor_comb.set("English")
##################################
chang_btn = Button(frame,text="Translate",relief=RAISED, command=data)
chang_btn.place(x=200,y=360,height=30,width=100)


######################################
sor_comb_dest = ttk.Combobox(frame,values=list_text)
sor_comb_dest.place(x=320,y=360,height=30,width=100)
sor_comb_dest.set("English")

######################
label_text = Label(root,text="Destination Text",font=("Time New Roman",15),bg="red")
label_text.place(x=125,y=420,height=40,width=250)


########################
dest_text = Text(frame,font=("Time New Roman",20),wrap=WORD)
dest_text.place(x=10,y=480,height=150,width=480)



root.mainloop()


