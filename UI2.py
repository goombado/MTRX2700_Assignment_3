import tkinter as tk
from tkinter import ttk


def beginScan() -> None:
    print("Begin Scan")


def checkoutFunc() -> None:
    top= tk.Toplevel(window)
    top.geometry("240x50")
    top.title("Checkout Window")
    tk.Label(top, text= "Testing Checkout").place(x=10,y=10)
    tk.Button(top, text= "Exit" , command = window.destroy).place(x=100,y=30)

window = tk.Tk()

# Get your screen resolution to calculate layout parameters
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
print(screenwidth, screenheight)

# Make the window half the size of the screen
width = int(screenwidth/2)
height = int(screenheight/2)

# Set the offset to center the window on the screen
offset_width = int((screenwidth-width)/2)
offset_height = int((screenheight-height)/2)

# Import parameters to the window to complete the window settings
window_size = f'{width}x{height}+{offset_width}+{offset_height}'
window.title('TEST1')
window.resizable(False,False) # command this line to open window resize
window.geometry(window_size)

# Insert frames to the top of the window
frame_top_height = int(height/9)
frame_top = tk.Frame(window, bg = 'SteelBlue1', width=width, height=frame_top_height)
label1 = tk.Label(frame_top, text='TEST2',bg='SteelBlue1', font=('Times New Roman',17,'bold'))
frame_top.place(x = 0, y = 0)
label1.place(relx = 0.25, rely = 0, relwidth = 0.5, relheight = 1)

# Create frame to the right of the window
frame_right_height = int(height - frame_top_height)
frame_right_width = int(width * 0.3)
frame_right = tk.Frame(window, bg = 'SteelBlue1', width=frame_right_width, height=frame_right_height)
offset_height = frame_top_height
offset_width = int(width - frame_right_width)
frame_right.place(x = offset_width, y = offset_height)

# Create frame to the right
frame_left_height= int(height - frame_top_height)
frame_left_width= int(width - frame_right_width)
frame_left = tk.Frame(window, bg = 'light cyan', width=frame_left_width, height=frame_left_height)
frame_left.place(x = 0, y = frame_top_height)



# Insert button to the right frame
button_width = int(0.7 * frame_right_width)
button_height = int(0.17 * frame_right_height)

checkout = tk.Button(
    frame_right,
    bg = 'midnight blue',
    fg = 'snow',
    highlightbackground="blue",
    activebackground = 'red2',
    text = "Checkout",
    font=('Times New Roman',17,'bold'),
    command = checkoutFunc,
)

button1 = tk.Button(
    frame_right,
    bg = 'midnight blue',
    fg = 'snow',
    highlightbackground="#000fff000",
    activebackground = 'red2',
    font=('Times New Roman',17,'bold'),
    text = "Scan",
    command=beginScan,
)

# Set buttons position 
x_offset = int((frame_right_width - button_width)/2)
y1_offset = (frame_right_height * 0.75)
y2_offset = (frame_right_height * 0.55)
checkout.place(x = x_offset , y = y1_offset , width= button_width, height= button_height)
button1.place(x = x_offset , y = y2_offset , width= button_width, height= button_height)

receipt = ttk.Treeview(frame_left, height = frame_left_height)
receipt['column'] = ('Item', 'Quantity', 'Price')

width = int(frame_left_width/3)
receipt.column("#0", width=0,  stretch=tk.NO)
receipt.column("Item",anchor=tk.CENTER, width = width)
receipt.column("Quantity",anchor=tk.CENTER,width=width)
receipt.column("Price",anchor=tk.CENTER,width=width)

receipt.heading("#0",text="",anchor=tk.CENTER)
receipt.heading("Item",text="Item",anchor=tk.CENTER)
receipt.heading("Quantity",text="Quantity",anchor=tk.CENTER)
receipt.heading("Price",text="Price",anchor=tk.CENTER)

receipt.place(x= 0, y= 0)

window.mainloop()
