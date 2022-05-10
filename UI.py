from tkinter import *
from tkinter import ttk


def beginScan() -> None:
    print("Begin Scan")


def checkoutFunc() -> None:
    top= Toplevel(window)
    top.geometry("240x50")
    top.title("Checkout Window")
    Label(top, text= "Testing Checkout").place(x=10,y=10)
    Button(top, text= "Exit" , command = window.destroy).place(x=100,y=30)



window = Tk()

myFrame = Frame(window, bg = "grey", height = 600 , width = 300)


checkout = Button(
    window,
    highlightbackground="blue",
    text = "Checkout",
    width=10,
    height=5,
    command = checkoutFunc,
)


button1 = Button(
    window,
    highlightbackground="#000fff000",
    text = "Scan",
    width=10,
    height=5,
    command=beginScan,
)

receipt = ttk.Treeview(window)

receipt['column'] = ('Item', 'Quantity', 'Price')

receipt.column("#0", width=0,  stretch=NO)
receipt.column("Item",anchor=CENTER, width=80)
receipt.column("Quantity",anchor=CENTER,width=80)
receipt.column("Price",anchor=CENTER,width=80)


receipt.heading("#0",text="",anchor=CENTER)
receipt.heading("Item",text="Item",anchor=CENTER)
receipt.heading("Quantity",text="Quantity",anchor=CENTER)
receipt.heading("Price",text="Price",anchor=CENTER)


myFrame.pack()
checkout.place(x = 180 , y = 400)
button1.place(x = 30 , y =400)
receipt.place(x= 30, y= 10)


window.mainloop()