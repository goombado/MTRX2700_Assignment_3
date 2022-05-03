import tkinter as tk

def beginScan() -> None:
    print("Begin Scan")


window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

checkout = tk.Label(
    text = "Checkout",
    foreground= "white",
    background= "black"
)
checkout.grid(row=0, column=0, sticky="n")


button1 = tk.Button(
    text = "Scan",
    width=25,
    height=5,
    activeforeground="white",
    command=beginScan,
)
button1.grid(row=1, column=0, sticky="n")

window.mainloop()