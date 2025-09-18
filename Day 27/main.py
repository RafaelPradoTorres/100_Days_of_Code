import tkinter
from _ast import arguments

window = tkinter.Tk()
window.title("OMG!! Hiii =)")
window.minsize(500, 300)
window.config(padx=20, pady=20)

#Label
my_label = tkinter.Label(text="This is a label", font=("Arial", 18, "bold"))
my_label.grid(column=0, row=0) #put the label on the screen


my_label["text"] = "New Text"
my_label.config(text="OMG!!! It's a new text!!!!")


#Button
def button_clicked():
    my_label.config(text = input.get())

def button2_clicked():
    my_label.config(text = "OMG!! You clicked me!!!!")

button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)


#Entry
input = tkinter.Entry(width = 10)
input.grid(column=4, row=2)

#New button
new_button = tkinter.Button(text="New Button", command=button2_clicked)
new_button.grid(column=2, row=0)

# TKinter positioning:
# Pack          -> apenas o sentido
# Place (x, y)  -> preciso demais (x, y)
# Grid          -> (column, row)







window.mainloop() #mantém a tela aberta
