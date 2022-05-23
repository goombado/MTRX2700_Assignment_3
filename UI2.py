from pickle import TRUE
import tkinter as tk
from tkinter import ttk
import serial
import time
from TempObjectDetect import main_object_detection 

# Variables for use
global uniqueItems
uniqueItems=0

def scan() -> None:
    global uniqueItems
    serialString = ""      
    serialPort = serial.Serial(port="COM4", baudrate=9600, bytesize=serial.EIGHTBITS, timeout=2, write_timeout = 0, xonxoff=True, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    time.sleep(0.1)   # Only needed for Arduino,For AVR/PIC/MSP430 & other Micros not needed
    BytesWritten1 = serialPort.write(b's')      #transmit 'A' (8bit) to micro/Arduino
    serialPort.flush()
    
    BytesWritten2 = serialPort.write(b'\r')      #transmit 'A' (8bit) to micro/Arduino
    serialPort.flush()
    
    BytesWritten3 = serialPort.write(b'\n')      #transmit 'A' (8bit) to micro/Arduino
    serialPort.flush()

    print("Begin Scan")
    
    detectedObject = main_object_detection(None, None, None)
    itemFound = False

    if uniqueItems != 0:
        for i in range(uniqueItems):
            object = receipt.item(i)
            values = object.get("values")
            if values[0] == detectedObject[0]:
                receipt.delete(i)
                receipt.insert(parent='',index='end',iid=i,text='',
                    values=(values[0],values[1] + 1,values[2]))
                itemFound == True
                return
    if itemFound == False:
        receipt.insert(parent='',index='end',iid=uniqueItems,text='',
            values=(detectedObject[0],'1',detectedObject[1]))
        uniqueItems = uniqueItems+1



def checkoutFunc() -> None:
    top= tk.Toplevel(window)
    top.geometry("260x330")
    top.title("Checkout Window")
    tk.Label(top, text= "Testing Checkout").place(x=80,y=10)

    receiptColumns = ('Item', 'Quantity', 'Price')
    finalReceipt = ttk.Treeview(top, columns = receiptColumns, show = 'headings')
    
    width = 80
    finalReceipt.column("#0", width=0,  stretch=tk.NO)
    finalReceipt.column("Item",anchor=tk.CENTER, width = width)
    finalReceipt.column("Quantity",anchor=tk.CENTER,width=width)
    finalReceipt.column("Price",anchor=tk.CENTER,width=width)

    finalReceipt.heading("#0",text="",anchor=tk.CENTER)
    finalReceipt.heading("Item",text="Item",anchor=tk.CENTER)
    finalReceipt.heading("Quantity",text="Quantity",anchor=tk.CENTER)
    finalReceipt.heading("Price",text="Price",anchor=tk.CENTER)

    finalReceipt.place(x=10,y=60)

    for i in range(uniqueItems):
        object = receipt.item(i)
        values = object.get("values")
        finalReceipt.insert(parent='',index='end',iid=i,text='',
            values=(values[0],values[1], values[2])) 
    
    tk.Button(top, text= "Exit" , command = window.destroy).place(x=120,y=300)

window = tk.Tk()


# Get your screen resolution to calculate layout parameters
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

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
frame_top.place(x = 0, y = 0)

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

# Create a label to the top frame
label1 = tk.Label(frame_top, text='Checkout',bg='SteelBlue1', font=('Times New Roman',17,'bold'))
label1.place(relx = 0.25, rely = 0, relwidth = 0.5, relheight = 1)

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
    command=scan,
)

# Set buttons position 
x_offset = int((frame_right_width - button_width)/2)
y1_offset = (frame_right_height * 0.75)
y2_offset = (frame_right_height * 0.55)
checkout.place(x = x_offset , y = y1_offset , width= button_width, height= button_height)
button1.place(x = x_offset , y = y2_offset , width= button_width, height= button_height)

# Create a table to the left frame
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
