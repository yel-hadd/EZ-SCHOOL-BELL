from tkinter import *

from tkinter import ttk


root = Tk()

root.title("Simple Treeview")
root.geometry("661x551")

tree = ttk.Treeview(root)
tree['show'] = 'headings'

tree['columns'] = ("ID", "DAY", "START_TIME", "DESCRIPTION")

tree.column("ID", anchor=CENTER, width=1, minwidth=2)
tree.column("DAY", anchor=W, width=40, minwidth=25)
tree.column("START_TIME", anchor=W, width=40, minwidth=25)
tree.column("DESCRIPTION", anchor=W, width=290, minwidth=25)


tree.heading("ID", text="ID", anchor=CENTER)
tree.heading("DAY", text="Jour", anchor=W)
tree.heading("START_TIME", text="Heure de début", anchor=W)
tree.heading("DESCRIPTION", text="Description", anchor=W)



tree.insert(parent='', index='end', iid=0, text='', values=("1", "Lundi", "00:00", "test alarm"))
tree.insert(parent='', index='end', iid=1, text='', values=("2", "Mardi", "00:00", "test alarm"))
tree.insert(parent='', index='end', iid=2, text='', values=("3", "Mardi", "00:00", "test alarm"))
tree.insert(parent='', index='end', iid=3, text='', values=("4", "Mercredi", "00:00", "test alarm"))
tree.insert(parent='', index='end', iid=4, text='', values=("5", "Jeudi", "00:00", "test alarm"))
tree.insert(parent='', index='end', iid=5, text='', values=("6", "Samedi", "00:00", "test alarm"))
tree.insert(parent='', index='end', iid=6, text='', values=("7", "Dimanche", "00:00", "test alarm"))
tree.insert(parent='', index='end', iid=7, text='', values=("8", "Lundi", "00:00", "test alarm"))
tree.insert(parent='', index='end', iid=8, text='', values=("1", "Lundi", "00:00", "test alarm"))
tree.insert(parent='', index='end', iid=9, text='', values=("1", "Lundi", "00:00", "test alarm"))
tree.insert(parent='', index='end', iid=10, text='', values=("1", "Lundi", "00:00", "test alarm"))
tree.insert(parent='', index='end', iid=11, text='', values=("1", "Lundi", "00:00", "test alarm"))
tree.insert(parent='', index='end', iid=12, text='', values=("1", "Lundi", "00:00", "test alarm"))








tree.place(x=29, y=288.36, width=602.89, height=211.68)

vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)

add_frame = Frame(root)


nl = Label(add_frame, text="Name")
nl.grid(row=0, column=0)

il = Label(add_frame, text="ID")
il.grid(row=0, column=0)

vsb.place(x=614, y=289, height=210)

tree.configure(yscrollcommand=vsb.set)

add_frame.place(x=50, y=50)
root.mainloop()
